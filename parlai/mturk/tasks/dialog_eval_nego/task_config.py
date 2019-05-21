#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

task_config = {}


task_config['frontend_version'] = 1

"""A short and descriptive title about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT title appears in search results,
and everywhere the HIT is mentioned.
"""
# task_config['hit_title'] = 'Ask and answer a question about a paragraph'
task_config['hit_title'] = 'Negotiation Dialog with a Robot'


"""A description includes detailed information about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT description appears in the expanded
view of search results, and in the HIT and assignment screens.
"""
# task_config['hit_description'] = 'Ask and answer a question about a paragraph.'
task_config['hit_description'] = 'Negotiate with a robot to divid some items'


"""One or more words or phrases that describe the HIT, separated by commas.
On MTurk website, these words are used in searches to find HITs.
"""
# task_config['hit_keywords'] = 'chat,question,answer'
task_config['hit_keywords'] = 'negotiation,dialog'


"""A detailed task description that will be shown on the HIT task preview page
and on the left side of the chat page. Supports HTML formatting.
"""
# task_config['task_description'] = \
# '''\'\'\'
# In this task, you will need to ask a question about a paragraph, and then provide your own answer to it.<br><br>
# Example:<br><br>
# ------------------- Task Begin ------------------- <br><br>
# <b>QA Collector</b>:<br>
# New Haven\'s greatest culinary claim to fame may be its pizza, which has been claimed to be among the best in the country, or even in the world. New Haven-style pizza, called "apizza" (pronounced ah-BEETS, [a'pitts] in the original Italian dialect), made its debut at the iconic Frank Pepe Pizzeria Napoletana (known as Pepe\'s) in 1925. Apizza is baked in coal- or wood-fired brick ovens, and is notable for its thin crust. Apizza may be red (with a tomato-based sauce) or white (with a sauce of garlic and olive oil), and pies ordered "plain" are made without the otherwise customary mozzarella cheese (originally smoked mozzarella, known as "scamorza" in Italian). A white clam pie is a well-known specialty of the restaurants on Wooster Street in the Little Italy section of New Haven, including Pepe\'s and Sally\'s Apizza (which opened in 1938). Modern Apizza on State Street, which opened in 1934, is also well-known.<br><br>Please provide a question given this context.<br><br>
# <b>Worker</b>:<br>
# What is apizza baked in?<br><br>
# <b>QA Collector</b>:<br>
# Thanks. And what is the answer to your question?<br><br>
# <b>Worker</b>:<br>
# It's baked in coal- or wood-fired brick ovens.<br><br>
# ------------------- Task Done ------------------- <br><br>
# If you are ready, please click "Accept HIT" to start this task.
# \'\'\''''
task_config['task_description'] = \
'''\'\'\'
In this task, you will need to negotiate with a robot throuth dialog. <br>
Your goal is to maximize the <b>total value of items</b> you can get. <br>
<b>In each dialog</b>, you will be shown the value of each item, and the number of each item. <b>Note</b> that the value for the robot can be different from yours.<br>
When each of you agree with the other's claim by saying, e.g., okay, the dialog terminates.
<br><br>
Example:<br>
------------------- Task Begin ------------------- <br>
<b>Value List</b><br>
<b>book</b> number: 3 value: 0 <br>
<b>hat</b> number: 1 value: 6 <br>
<b>ball</b> number: 1 value: 4 <br><br>

<b>Bot</b>: i would like the hat and the ball<br>
<b>You</b>: i need the ball and the hat<br>
<b>Bot</b>: i really need the hat, but you can have the rest<br>
<b>You</b>: i need the hat and the ball<br>
<b>Bot</b>: okay<br>

------------------- Task Done ------------------- <br><br>
If you are ready, please click "Accept HIT" to start this task.
\'\'\''''