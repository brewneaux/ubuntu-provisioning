import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dotfiles_folder_exists(host):
    f = host.file('/home/testuser/dotfiles')
    assert f.is_directory


def test_dircolors(host):
    f = host.file('/home/testuser/dotfiles/dircolors/dircolors.256dark')
    assert f.exists
    assert f.content_string


def test_zsh_files(host):
    rc = host.file('/home/testuser/dotfiles/zsh/zshrc')
    completion = host.file('/home/testuser/dotfiles/zsh/zsh_completion')
    assert rc.exists
    assert completion.exists
    assert rc.content_string
    assert completion.content_string

    rc_symlink = host.file('/home/testuser/.zshrc')
    assert rc_symlink.exists
    assert rc_symlink.content_string
    assert rc_symlink.is_symlink
    
def test_tmux_exists(host):
    f = host.file('/home/testuser/dotfiles/tmux.conf')
    assert f.exists
    assert f.content_string

    tmux_symlink = host.file('/home/testuser/.tmux.conf')
    assert tmux_symlink.exists
    assert tmux_symlink.content_string
    assert tmux_symlink.is_symlink

def test_vimrc(host):
    f = host.file('/home/testuser/dotfiles/vim/vimrc')
    assert f.exists
    assert f.content_string

    vimrc_symlink = host.file('/home/testuser/.vimrc')
    assert vimrc_symlink.exists
    assert vimrc_symlink.content_string
    assert vimrc_symlink.is_symlink

def test_zshrc_exists(host):
    f = host.file('/home/testuser/.zshrc')
    assert f.exists
    assert f.content_string

