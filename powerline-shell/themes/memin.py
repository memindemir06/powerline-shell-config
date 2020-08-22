# this theme file is in "~/.config/powerline-shell/themes/memin.py"

from powerline_shell.themes.default import DefaultColor

class Color(DefaultColor):
    USERNAME_FG = 3
    USERNAME_BG = 0
    USERNAME_ROOT_BG = 209

    HOSTNAME_FG = 3
    HOSTNAME_BG = 0

    HOME_SPECIAL_DISPLAY = False
    HOME_BG = 15
    HOME_FG = 3
    PATH_FG = 3
    PATH_BG = 15
    CWD_FG = 3
    SEPARATOR_FG = 251

    READONLY_BG = 209
    READONLY_FG = 15

    SSH_BG = 209
    SSH_FG = 15

    REPO_CLEAN_FG = 3
    REPO_CLEAN_BG = 15
    REPO_DIRTY_FG = 15
    REPO_DIRTY_BG = 196

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_FG = 15
    CMD_PASSED_BG = 196
    CMD_FAILED_FG = 15
    CMD_FAILED_BG = 1

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    GIT_AHEAD_BG = 3
    GIT_AHEAD_FG = 15
    GIT_BEHIND_BG = 1
    GIT_BEHIND_FG = 15
    GIT_STAGED_BG = 76
    GIT_STAGED_FG = 15
    GIT_NOTSTAGED_BG = 226
    GIT_NOTSTAGED_FG = 15
    #GIT_UNTRACKED_BG = 196
    #GIT_UNTRACKED_FG = 15
    #GIT_CONFLICTED_BG = 196
    #GIT_CONFLICTED_FG = 15
    #GIT_STASH_BG = 196
    #GIT_STASH_FG = 15

    VIRTUAL_ENV_BG = 255
    VIRTUAL_ENV_FG = 3

    BATTERY_NORMAL_BG = 255
    BATTERY_NORMAL_FG = 76
    BATTERY_LOW_BG = 255
    BATTERY_LOW_FG = 160

    AWS_PROFILE_FG = 15
    AWS_PROFILE_BG = 196

    TIME_FG = 0
    TIME_BG = 15
