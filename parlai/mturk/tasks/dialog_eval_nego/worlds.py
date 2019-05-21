#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from parlai.core.worlds import validate
from parlai.mturk.core.worlds import MTurkOnboardWorld, MTurkTaskWorld
from parlai.mturk.tasks.task_util import DialogSession, Log, TERMINAL_TAGS


class DialogEvalNegoOnboardWorld(MTurkOnboardWorld):
    '''Example onboarding world. Sends a message from the world to the
    worker and then exits as complete
    '''
    def parley(self):
        ad = {}
        ad['id'] = 'System'
        ad['text'] = 'Welcome onboard!'
        self.mturk_agent.observe(ad)
        self.mturk_agent.act()
        self.episodeDone = True


class DialogEvalNegoWorld(MTurkTaskWorld):
    """
    World for recording a turker's question and answer given a context.
    Assumes the context is a random context from a given task, e.g.
    from SQuAD, CBT, etc.
    """

    collector_agent_id = 'QA Collector'

    def __init__(self, opt, task, mturk_agent):
        self.task = task
        self.mturk_agent = mturk_agent
        self.episodeDone = False
        self.turn_index = -1
        self.context =  'context placeholder'
        self.question = 'question placeholder'
        self.answer = 'answer placeholder'

        # self-defined parameters
        self.max_turn_num = 10

        self.session = DialogSession()
        self.logger = Log('../tasks/dialog_eval_nego/log/dialog_logs.txt')

    def parley(self):
        # Each turn starts from the QA Collector agent
        self.turn_index = self.turn_index + 1
        ad = {'episode_done': False}
        ad['id'] = self.__class__.collector_agent_id

        if self.turn_index == 0:
            # At the first turn, gives both the context information and system utterances.
            context = 'this is context information'
            sys_uttr = 'system utterance [{}]'.format(self.turn_index)
            sys_response = '\n\n'.join([context, sys_uttr])

            ad['text'] = sys_response

            self.mturk_agent.observe(validate(ad))
            usr_action = self.mturk_agent.act()
            usr_uttr = usr_action['text']

            self.session.append(sys_uttr, usr_uttr)

        else:
            sys_uttr = 'system utterance [{}]'.format(self.turn_index)
            if self.turn_index == 5:
                sys_uttr = 'end'
            ad['text'] = sys_uttr

            for tag in TERMINAL_TAGS:
                if tag in sys_uttr:
                    reduced_uttr = sys_uttr.replace(' ', '')
                    if float(len(tag)) / float(len(reduced_uttr)) > 0.5:
                        self.episodeDone = True
                        ad['episode_done'] = True
                        break

            if self.episodeDone:
                self.mturk_agent.observe(validate(ad))
                self.session.append(sys_uttr, '<end turn>')
            else:
                self.mturk_agent.observe(validate(ad))
                usr_action = self.mturk_agent.act()
                usr_uttr = usr_action['text']

                self.session.append(sys_uttr, usr_uttr)

                for tag in TERMINAL_TAGS:
                    if tag in usr_uttr:
                        reduced_uttr = usr_uttr.replace(' ', '')
                        if float(len(tag)) / float(len(reduced_uttr)) > 0.5:
                            self.episodeDone = True


            if self.episodeDone:
                self.logger.log(self.session.get_history(), 'tag placeholder')
            # self.logger.log(self.session.get_history(), 'tag placeholder')



    def episode_done(self):
        return self.episodeDone

    def shutdown(self):
        self.task.shutdown()
        self.mturk_agent.shutdown()

    def review_work(self):
        # Can review the work here to accept or reject it
        pass

    def get_custom_task_data(self):
        # brings important data together for the task, to later be used for
        # creating the dataset. If data requires pickling, put it in a field
        # called 'needs-pickle'.
        return {
            'context': self.context,
            'acts': [self.question, self.answer],
        }
