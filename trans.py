stateList = [
    "entry",
    "rand_diff",
    "rand_diff_easy",
    "rand_diff_normal",
    "rand_diff_hard",
    "rand_diff_oni",
    "rand_oniA",
    "rand_oniB",
    "rand_oniC",
    "rand_oniD",
    "rand_hardA",
    "rand_hardB",
    "rand_hardC",
    "rand_hardD",
    "rand_normalA",
    "rand_normalB",
    "rand_normalC",
    "rand_easyA",
    "seeSheet"
]
transList = [
    {
        "trigger": "advance",
        "source": "entry",
        "dest": "rand_diff",
        "conditions": "is_going_to_rand_diff",
    },
    {
        "trigger": "reset",
        "source": ["entry", "rand_diff", 
                   "rand_diff_easy", "rand_diff_normal", "rand_diff_hard", "rand_diff_oni", 
                   "rand_oniA", "rand_oniB", "rand_oniC", "rand_oniD",
                   "rand_hardA", "rand_hardB", "rand_hardC", "rand_hardD",
                   "rand_normalA", "rand_normalB", "rand_normalC", "rand_easyA",
                   "seeSheet"
        ],
        "dest": "entry",
        "conditions": "return_to_entry"
    },
    {
        "trigger": "toDiff",
        "source": "rand_diff",
        "dest": "rand_diff_easy",
        "conditions": "choose_easy"
    },
    {
        "trigger": "toDiff",
        "source": "rand_diff",
        "dest": "rand_diff_normal",
        "conditions": "choose_normal"
    },
    {
        "trigger": "toDiff",
        "source": "rand_diff",
        "dest": "rand_diff_hard",
        "conditions": "choose_hard"
    },
    {
        "trigger": "toDiff",
        "source": "rand_diff",
        "dest": "rand_diff_oni",
        "conditions": "choose_oni"
    },
    {
        "trigger": "rand_oni_advance",
        "source": ["rand_diff_oni", "rand_oniA"],
        "dest": "rand_oniA",
        "conditions": "advance10"
    },
    {
        "trigger": "rand_oni_advance",
        "source": ["rand_diff_oni", "rand_oniB"],
        "dest": "rand_oniB",
        "conditions": "advance89"
    },
    {
        "trigger": "rand_oni_advance",
        "source": ["rand_diff_oni", "rand_oniC"],
        "dest": "rand_oniC",
        "conditions": "advance68"
    },
    {
        "trigger": "rand_oni_advance",
        "source": ["rand_diff_oni", "rand_oniD"],
        "dest": "rand_oniD",
        "conditions": "advance16"
    },
    {
        "trigger": "rand_hard_advance",
        "source": ["rand_diff_hard", "rand_hardA"],
        "dest": "rand_hardA",
        "conditions": "advance8"
    },
    {
        "trigger": "rand_hard_advance",
        "source": ["rand_diff_hard", "rand_hardB"],
        "dest": "rand_hardB",
        "conditions": "advance78"
    },
    {
        "trigger": "rand_hard_advance",
        "source": ["rand_diff_hard", "rand_hardC"],
        "dest": "rand_hardC",
        "conditions": "advance57"
    },
    {
        "trigger": "rand_hard_advance",
        "source": ["rand_diff_hard", "rand_hardD"],
        "dest": "rand_hardD",
        "conditions": "advance15"
    },
    {
        "trigger": "rand_normal_advance",
        "source": ["rand_diff_normal", "rand_normalA"],
        "dest": "rand_normalA",
        "conditions": "advance7"
    },
    {
        "trigger": "rand_normal_advance",
        "source": ["rand_diff_normal", "rand_normalB"],
        "dest": "rand_normalB",
        "conditions": "advance57"
    },
    {
        "trigger": "rand_normal_advance",
        "source": ["rand_diff_normal", "rand_normalC"],
        "dest": "rand_normalC",
        "conditions": "advance15"
    },
    {
        "trigger": "rand_easy_advance",
        "source": ["rand_diff_easy", "rand_easyA"],
        "dest": "rand_easyA",
        "conditions": "advance15"
    },
    {
        "trigger": "sheet",
        "source": ["rand_oniA", "rand_oniB", "rand_oniC", "rand_oniD",
                   "rand_hardA", "rand_hardB", "rand_hardC", "rand_hardD",
                   "rand_normalA", "rand_normalB", "rand_normalC", "rand_easyA"
        ],
        "dest": "seeSheet",
        "conditions": "to_seeSheet"
    }
    # {"trigger": "go_back", "source": ["rand_diff", "state2"], "dest": "entry"},
]

# Transcition template
# {
#     "trigger": "",
#     "source": "",
#     "dest": "",
#     "conditions": ""
# }