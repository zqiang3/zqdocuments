set nu                          "设置行号

set tabstop=4                   "设置tab键宽度
set expandtab                   "将tab转换为空格

set autoindent                  "自动缩进 take indent for new linefrom previous line
set noswapfile                  "禁止生成临时文件

set mouse=a                     "可以在buffer的任何地方使用鼠标

imap <C-e> <END>
imap <C-a> <HOME>
imap <C-u> <esc>d0i
imap <C-k> <esc>d$i

inoremap { {<CR>}<Esc>ka<CR><tab>
inoremap ( ()<left>
inoremap " ""<left>

map <C-a> ggVG

let g:neocomplcache_enable_at_startup = 1
let g:neocomplcache_enalbe_auto_select = 1