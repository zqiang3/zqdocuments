set nu          "设置行号
set tabstop=4	"设置tab键宽度
set expandtab	"将tab转换为空格
set softtabstop=4	"BS时，4个空白当作一个tab删除
set shiftwidth=4	"每一级缩进的长度
set autoindent	"自动缩进
set cindent 	"针对c语言自动缩进

set nocp
filetype plugin on

set cursorline
set ignorecase smartcase
set nocompatible
set noswapfile 	"禁止生成临时文件
set t_Co=256
colorscheme molokai

map <C-a> ggVG
map <C-c> "+y

autocmd BufNewFile *  setlocal filetype=html
function! InsertHtmlTag()
    let pat = '\c<\w\+\s*\(\s\+\w\+\s*=\s*[''#$;,()."a-z0-9]\+\)*\s*>'
    normal! a>
    let save_cursor = getpos('.')
    let result = matchstr(getline(save_cursor[1]), pat)
    "if (search(pat, 'b', save_cursor[1]) && searchpair('<','','>','bn',0,  getline('.')) > 0)
    if (search(pat, 'b', save_cursor[1]))
        normal! lyiwf>
        normal! a</
        normal! p
        normal! a>
    endif
    :call cursor(save_cursor[1], save_cursor[2], save_cursor[3])
endfunction
"inoremap > <ESC>:call InsertHtmlTag()<CR>a

let g:neocomplcache_enable_at_startup = 1
let g:neocomplcache_enable_auto_select = 1

inoremap ( ()<Esc>i
inoremap [ []<Esc>i
""inoremap { {}<Esc>i
""inoremap <C-\> {}<Left>
""inoremap { {}<Esc>i<Enter><Up><Right><Enter>
inoremap ' ''<Esc>i
inoremap " ""<Esc>i
"inoremap < <><Esc>i

" C的编译和运行
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
exec "w"
exec "!gcc % -g -o %<"
exec "! ./%<"
endfunc

" C++的编译和运行
map <F6> :call CompileRunGpp()<CR>
func! CompileRunGpp()
exec "w"
exec "!g++ % -g -o %<"
exec "! ./%<"
endfunc

" Python脚本运行"
map <F8> :call RunPython()<CR>
func! RunPython()
exec "w"
exec "!python %"
endfunc
