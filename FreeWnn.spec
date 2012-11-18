Summary:	FreeWnn Japanese Input System
Summary(pl.UTF-8):	FreeWnn - system wprowadzania znaków japońskich
Name:		FreeWnn
Version:	1.1.1
%define	subver	a021
Release:	0.%{subver}.2
Epoch:		2
License:	LGPL v2+ (libraries), GPL v2+ (programs)
Group:		Applications/System
#Source0Download: http://sourceforge.jp/projects/freewnn/releases/
Source0:	http://dl.sourceforge.jp/freewnn/17724/%{name}-%{version}-%{subver}.tar.bz2
# Source0-md5:	7e15ab385932d58e3743400d303a05e6
Source1:	%{name}.init
Source2:	%{name}-cWnn.init
Source3:	%{name}-tWnn.init
Source4:	%{name}-kWnn.init
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-ja.patch
Patch2:		%{name}-noroot.patch
Patch3:		%{name}-jserverrc-g-jinmei.patch
Patch4:		%{name}-reuid.patch
Patch5:		%{name}-manpaths.patch
Patch6:		%{name}-libtool.patch
Patch7:		%{name}-cpp.patch
Patch8:		%{name}-install.patch
Patch9:		%{name}-link.patch
Patch10:	%{name}-format.patch
URL:		http://www.freewnn.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	setup >= 2.4.1
Conflicts:	wnn6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/FreeWnn

%description
This distribution contains FreeWnn Japanese Input System. FreeWnn is a
network-extensible Kana-to-Kanji conversion system and was jointly
developed and released by the Software Research Group of Kyoto
University Research Institute for Mathematical Science, OMRON
Corporation and Astec, Inc.

%description -l pl.UTF-8
Ten pakiet zawiera system wprowadzania znaków japońskich FreeWnn. Jest
to, działający także przez sieć, system konwersji Kana do Kanji,
stworzony i rozwijany wspólnie przez Software Research Group z
Institute for Mathematical Science Kyoto University, OMRON Corporation
oraz Astec, Inc.

%package libs
Summary:	Runtime library for FreeWnn
Summary(pl.UTF-8):	Biblioteki współdzielone FreeWnn
Group:		Libraries

%description libs
This package contains the runtime library for running programs with
FreeWnn.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone FreeWnn.

%package devel
Summary:	Header files for FreeWnn
Summary(pl.UTF-8):	Pliki nagłówkowe FreeWnn
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files for building programs with use
FreeWnn.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do budowania programów
używających FreeWnn.

%package static
Summary:	Static FreeWnn library
Summary(pl.UTF-8):	Statyczna biblioteka FreeWnn
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of FreeWnn library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki FreeWnn.

%package common
Summary:	Common files for Wnn
Summary(pl.UTF-8):	Wspólne pliki Wnn
Group:		Applications/System
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Provides:	group(wnn)
Provides:	user(wnn)

%description common
FreeWnn-common includes the files you need to run FreeWnn, cWnn or
kWnn.

%description common -l pl.UTF-8
Ten pakiet zawiera wspólne pliki niezbędne do uruchomienia FreeWnn,
cWnn lub kWnn.

%package -n cWnn
Summary:	cWnn Chinese Input System (version for China)
Summary(pl.UTF-8):	cWnn System wprowadzania znaków chińskich (wersja dla Chin)
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	cWnn-common = %{epoch}:%{version}-%{release}
Requires:	setup >= 2.4.1-3

%description -n cWnn
This package includes FreeWnn Chinese Input System (version for
China).

%description -n cWnn -l pl.UTF-8
Ten pakiet zawiera system wprowadzania znaków chińskich FreeWnn w
wersji dla Chin.

%package -n cWnn-common
Summary:	cWnn/tWnn Chinese Input System common files
Summary(pl.UTF-8):	Wspólne pliki systemu wprowadzania znaków chińskich cWnn/tWnn
Group:		Applications/System
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	cWnn-libs = %{epoch}:%{version}-%{release}

%description -n cWnn-common
This package includes cWnn/tWnn Chinese Input System common files for
China and Taiwan version.

%description -n cWnn-common -l pl.UTF-8
Ten pakiet zawiera pliki wspólne dla wersji chińskiej i tajwańskiej
systemu wprowadzania znaków chińskich cWnn/tWnn.

%package -n cWnn-libs
Summary:	cWnn/tWnn runtime library
Summary(pl.UTF-8):	Biblioteka współdzielona cWnn/tWnn
Group:		Libraries

%description -n cWnn-libs
This package contains cWnn/tWnn runtime library.

%description -n cWnn-libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną cWnn/tWnn.

%package -n cWnn-devel
Summary:	Header files for cWnn/tWnn
Summary(pl.UTF-8):	Pliki nagłówkowe cWnn/tWnn
Group:		Development/Libraries
Requires:	cWnn-libs = %{epoch}:%{version}-%{release}

%description -n cWnn-devel
This package contains the header files for building programs with use
cWnn/tWnn.

%description -n cWnn-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do budowania programów używających
cWnn/tWnn.

%package -n cWnn-static
Summary:	Static cWnn/tWnn library
Summary(pl.UTF-8):	Statyczna biblioteka cWnn/tWnn
Group:		Development/Libraries
Requires:	cWnn-devel = %{epoch}:%{version}-%{release}

%description -n cWnn-static
This package contains static version of cWnn/tWnn library.

%description -n cWnn-static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki cWnn/tWnn.

%package -n tWnn
Summary:	tWnn Chinese Input System (version for Taiwan)
Summary(pl.UTF-8):	System wprowadzania znaków chińskich tWnn (wersja dla Tajwanu)
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	cWnn-common = %{epoch}:%{version}-%{release}
Requires:	setup >= 2.4.1-3

%description -n tWnn
FreeWnn Chinese Input System (version for Taiwan).

%description -n tWnn -l pl.UTF-8
System wprowadzania znaków chińskich FreeWnn w wersji dla Tajwanu.

%package -n kWnn
Summary:	kWnn Korean Input System
Summary(pl.UTF-8):	System wprowadzania znaków koreańskich kWnn
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	kWnn-libs = %{epoch}:%{version}-%{release}
Requires:	setup >= 2.4.1-3

%description -n kWnn
FreeWnn Korean Input System.

%description -n kWnn -l pl.UTF-8
System wprowadzania znaków koreańskich FreeWnn.

%package -n kWnn-libs
Summary:	kWnn runtime library
Summary(pl.UTF-8):	Biblioteka współdzielona kWnn
Group:		Libraries

%description -n kWnn-libs
This package contains kWnn runtime library.

%description -n kWnn-libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną kWnn.

%package -n kWnn-devel
Summary:	Header files for kWnn
Summary(pl.UTF-8):	Pliki nagłówkowe kWnn
Group:		Development/Libraries
Requires:	kWnn-libs = %{epoch}:%{version}-%{release}

%description -n kWnn-devel
This package contains the header files for building programs which use
kWnn.

%description -n kWnn-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do budowania programów używających
kWnn.

%package -n kWnn-static
Summary:	Static kWnn library
Summary(pl.UTF-8):	Statyczna biblioteka kWnn
Group:		Development/Libraries
Requires:	kWnn-devel = %{epoch}:%{version}-%{release}

%description -n kWnn-static
This package contains static version of kWnn library.

%description -n kWnn-static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki kWnn.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

cp -p Wnn-consortium/dic/README README.Wnn-consortium.dic

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

# Makefile is missing for en manuals - install manually
for f in atod atof dtoa ; do
	install -D Wnn/man.en/6.jutil/${f}.man $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/FreeWnn
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/cWnn
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/tWnn
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/kWnn

ln -sf /var/lib/wnn/ja/dic $RPM_BUILD_ROOT%{_sysconfdir}/ja/dic
ln -sf /var/lib/wnn/zh_CN/dic $RPM_BUILD_ROOT%{_sysconfdir}/zh_CN/dic
ln -sf /var/lib/wnn/zh_TW/dic $RPM_BUILD_ROOT%{_sysconfdir}/zh_TW/dic
ln -sf /var/lib/wnn/ko_KR/dic $RPM_BUILD_ROOT%{_sysconfdir}/ko_KR/dic

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/wnntouch /var/lib/wnn/ja/dic/gerodic/g-jinmei.dic
cd /var/lib/wnn/ja/dic/pubdic
%{_bindir}/wnntouch *.*
/sbin/chkconfig --add FreeWnn
%service FreeWnn restart

%preun
if [ "$1" = "0" ]; then
	%service FreeWnn stop
	/sbin/chkconfig --del FreeWnn
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post -n cWnn
cd /var/lib/wnn/zh_CN/dic/sys
%{_bindir}/cwnntouch *.*
/sbin/chkconfig --add cWnn
%service cWnn restart

%preun -n cWnn
if [ "$1" = "0" ]; then
	%service cWnn stop
	/sbin/chkconfig --del cWnn
fi

%post	-n cWnn-libs -p /sbin/ldconfig
%postun	-n cWnn-libs -p /sbin/ldconfig

%post -n tWnn
cd /var/lib/wnn/zh_TW/dic/sys
%{_bindir}/cwnntouch *.*
/sbin/chkconfig --add tWnn
%service tWnn restart

%preun -n tWnn
if [ "$1" = "0" ]; then
	%service tWnn stop
	/sbin/chkconfig --del tWnn
fi

%post -n kWnn
cd /var/lib/wnn/ko_KR/dic/sys
%{_bindir}/kwnntouch *.*
/sbin/chkconfig --add kWnn
%service kWnn restart

%preun -n kWnn
if [ "$1" = "0" ]; then
	%service kWnn stop
	/sbin/chkconfig --del kWnn
fi

%post	-n kWnn-libs -p /sbin/ldconfig
%postun	-n kWnn-libs -p /sbin/ldconfig

%pre common
%groupadd -P %{name}-common -g 42 wnn
%useradd -P %{name}-common -u 42 -c "Wnn Service User" -g wnn -s /bin/false wnn

%postun common
if [ "$1" = "0" ]; then
	%userremove wnn
	%groupremove wnn
fi

%files
%defattr(644,root,root,755)
%doc Contrib/dic/gerodic/GERODIC PubdicPlus/PUBDICPLUS-README Wnn/manual.en
%lang(ja) %doc PubdicPlus/{PUBDICPLUS-ERRATA,PUBDICPLUS-README.jp} Wnn/manual README.Wnn-consortium.dic
%attr(754,root,root) /etc/rc.d/init.d/FreeWnn
%attr(755,root,root) %{_bindir}/atod
%attr(755,root,root) %{_bindir}/atof
%attr(755,root,root) %{_bindir}/dtoa
%attr(755,root,root) %{_bindir}/jserver
%attr(755,root,root) %{_bindir}/oldatonewa
%attr(755,root,root) %{_bindir}/wddel
%attr(755,root,root) %{_bindir}/wdreg
%attr(755,root,root) %{_bindir}/wnnkill
%attr(755,root,root) %{_bindir}/wnnstat
%attr(755,root,root) %{_bindir}/wnntouch
%{_mandir}/man1/atod.1*
%{_mandir}/man1/atof.1*
%{_mandir}/man1/dtoa.1*
%lang(ja) %{_mandir}/ja/man1/atod.1*
%lang(ja) %{_mandir}/ja/man1/atof.1*
%lang(ja) %{_mandir}/ja/man1/dtoa.1*
%lang(ja) %{_mandir}/ja/man1/jserver.1*
%lang(ja) %{_mandir}/ja/man1/oldatonewa.1*
%lang(ja) %{_mandir}/ja/man1/uum.1*
%lang(ja) %{_mandir}/ja/man1/wddel.1*
%lang(ja) %{_mandir}/ja/man1/wdreg.1*
%lang(ja) %{_mandir}/ja/man1/wnnkill.1*
%lang(ja) %{_mandir}/ja/man1/wnnstat.1*
%lang(ja) %{_mandir}/ja/man1/wnntouch.1*
%lang(ja) %{_mandir}/ja/man4/2a_ctrl.4*
%lang(ja) %{_mandir}/ja/man4/2b_romkana.4*
%lang(ja) %{_mandir}/ja/man4/cvt_key_tbl.4*
%lang(ja) %{_mandir}/ja/man4/fzk.data.4*
%lang(ja) %{_mandir}/ja/man4/fzk.u.4*
%lang(ja) %{_mandir}/ja/man4/hinsi_data.4*
%lang(ja) %{_mandir}/ja/man4/jserverrc.4*
%lang(ja) %{_mandir}/ja/man4/mode.4*
%lang(ja) %{_mandir}/ja/man4/serverdefs.4*
%lang(ja) %{_mandir}/ja/man4/ujis_dic.4*
%lang(ja) %{_mandir}/ja/man4/uumkey.4*
%lang(ja) %{_mandir}/ja/man4/uumrc.4*
%lang(ja) %{_mandir}/ja/man4/wnnenvrc.4*
%lang(ja) %{_mandir}/ja/man5/pubdic.5*
%lang(ja) %{_mandir}/ja/man5/usr_dic.5*
%dir %{_sysconfdir}/ja
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ja/hinsi.data
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ja/jserverrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ja/uumkey*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ja/uumrc*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ja/wnnenvrc*
%{_sysconfdir}/ja/libwnn.msg
%{_sysconfdir}/ja/uum.msg
%{_sysconfdir}/ja/wnnstat.msg
%{_sysconfdir}/ja/dic
%{_sysconfdir}/ja/rk
%{_sysconfdir}/ja/rk.vi
%dir %{_sysconfdir}/lt_LN
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lt_LN/uumkey*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lt_LN/uumrc*
%{_sysconfdir}/lt_LN/uum.msg
%{_sysconfdir}/lt_LN/rk
%dir /var/lib/wnn/ja
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic/gerodic
%attr(664,root,wnn) /var/lib/wnn/ja/dic/gerodic/g-jinmei.dic
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic/pubdic
%attr(664,root,wnn) /var/lib/wnn/ja/dic/pubdic/*.dic
%attr(664,root,wnn) /var/lib/wnn/ja/dic/pubdic/*.fzk
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic/src
%attr(664,root,wnn) /var/lib/wnn/ja/dic/src/fzk.*
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic/wnncons
%attr(664,root,wnn) /var/lib/wnn/ja/dic/wnncons/tankan*.dic

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjd.so.0
%attr(755,root,root) %{_libdir}/libwnn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwnn.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjd.so
%attr(755,root,root) %{_libdir}/libwnn.so
%{_libdir}/libjd.la
%{_libdir}/libwnn.la
%{_includedir}/wnn
%lang(ja) %{_mandir}/ja/man3/jl_*.3*
%lang(ja) %{_mandir}/ja/man3/js_*.3*
%lang(ja) %{_mandir}/ja/man3/msg_*.3*
%lang(ja) %{_mandir}/ja/man3/romkan_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libjd.a
%{_libdir}/libwnn.a

%files common
%defattr(644,root,root,755)
%doc CONTRIBUTORS ChangeLog.en Xwnmo/manual.en
%lang(ja) %doc ChangeLog Xwnmo/manual
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cvt_key_empty
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cvt_key_tbl*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/serverdefs
%dir /var/lib/wnn

%files -n cWnn
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/cWnn
%attr(755,root,root) %{_bindir}/cserver
%dir %{_sysconfdir}/zh_CN
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_CN/cixing.data
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_CN/cserverrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_CN/uumkey*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_CN/uumrc*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_CN/wnnenvrc*
%{_sysconfdir}/zh_CN/libwnn.msg
%{_sysconfdir}/zh_CN/uum.msg
%{_sysconfdir}/zh_CN/wnnstat.msg
%{_sysconfdir}/zh_CN/dic
%{_sysconfdir}/zh_CN/rk
%{_sysconfdir}/zh_CN/rk_p
%{_sysconfdir}/zh_CN/rk_z
%dir /var/lib/wnn/zh_CN
%attr(775,root,wnn) %dir /var/lib/wnn/zh_CN/dic
%attr(775,root,wnn) %dir /var/lib/wnn/zh_CN/dic/sys
%attr(664,root,wnn) /var/lib/wnn/zh_CN/dic/sys/*.dic
%attr(664,root,wnn) /var/lib/wnn/zh_CN/dic/sys/full.con*
%{_mandir}/man1/cserver.1*

%files -n cWnn-common
%defattr(644,root,root,755)
%doc cWnn/manual.en
%lang(ja) %doc cWnn/manual
%attr(755,root,root) %{_bindir}/catod
%attr(755,root,root) %{_bindir}/catof
%attr(755,root,root) %{_bindir}/cdtoa
%attr(755,root,root) %{_bindir}/cwddel
%attr(755,root,root) %{_bindir}/cwdreg
%attr(755,root,root) %{_bindir}/cwnnkill
%attr(755,root,root) %{_bindir}/cwnnstat
%attr(755,root,root) %{_bindir}/cwnntouch
%{_mandir}/man1/catod.1*
%{_mandir}/man1/catof.1*
%{_mandir}/man1/cdicsort.1*
%{_mandir}/man1/cdtoa.1*
%{_mandir}/man1/cuum.1*
%{_mandir}/man1/cwddel.1*
%{_mandir}/man1/cwdreg.1*
%{_mandir}/man1/cwnnkill.1*
%{_mandir}/man1/cwnnstat.1*
%{_mandir}/man1/cwnntouch.1*
%{_mandir}/man4/cenv.4*
%{_mandir}/man4/ckey.4*
%{_mandir}/man4/cst_end.4*
%{_mandir}/man4/cwnn.4*

%files -n cWnn-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcwnn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcwnn.so.0

%files -n cWnn-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcwnn.so
%{_libdir}/libcwnn.la
%{_includedir}/cwnn

%files -n cWnn-static
%defattr(644,root,root,755)
%{_libdir}/libcwnn.a

%files -n tWnn
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/tWnn
%attr(755,root,root) %{_bindir}/tserver
%dir %{_sysconfdir}/zh_TW
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_TW/cixing.data
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_TW/tserverrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_TW/uumkey*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_TW/uumrc*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zh_TW/wnnenvrc*
%{_sysconfdir}/zh_TW/libwnn.msg
%{_sysconfdir}/zh_TW/uum.msg
%{_sysconfdir}/zh_TW/wnnstat.msg
%{_sysconfdir}/zh_TW/dic
%{_sysconfdir}/zh_TW/rk
%{_sysconfdir}/zh_TW/rk_p
%{_sysconfdir}/zh_TW/rk_z
%dir /var/lib/wnn/zh_TW
%attr(775,root,wnn) %dir /var/lib/wnn/zh_TW/dic
%attr(775,root,wnn) %dir /var/lib/wnn/zh_TW/dic/sys
%attr(664,root,wnn) /var/lib/wnn/zh_TW/dic/sys/*.dic
%attr(664,root,wnn) /var/lib/wnn/zh_TW/dic/sys/full.con*

%files -n kWnn
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kWnn
%attr(755,root,root) %{_bindir}/katod
%attr(755,root,root) %{_bindir}/katof
%attr(755,root,root) %{_bindir}/kdtoa
%attr(755,root,root) %{_bindir}/kserver
%attr(755,root,root) %{_bindir}/kwddel
%attr(755,root,root) %{_bindir}/kwdreg
%attr(755,root,root) %{_bindir}/kwnnkill
%attr(755,root,root) %{_bindir}/kwnnstat
%attr(755,root,root) %{_bindir}/kwnntouch
%dir %{_sysconfdir}/ko_KR
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ko_KR/hinsi.data
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ko_KR/kserverrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ko_KR/uumkey
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ko_KR/uumrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ko_KR/wnnenvrc*
%{_sysconfdir}/ko_KR/libwnn.msg
%{_sysconfdir}/ko_KR/uum.msg
%{_sysconfdir}/ko_KR/wnnstat.msg
%{_sysconfdir}/ko_KR/dic
%{_sysconfdir}/ko_KR/rk
%dir /var/lib/wnn/ko_KR
%attr(775,root,wnn) %dir /var/lib/wnn/ko_KR/dic
%attr(775,root,wnn) %dir /var/lib/wnn/ko_KR/dic/sys
%attr(664,root,wnn) /var/lib/wnn/ko_KR/dic/sys/*.dic
%attr(664,root,wnn) /var/lib/wnn/ko_KR/dic/sys/full.fzk

%files -n kWnn-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkwnn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwnn.so.0

%files -n kWnn-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkwnn.so
%{_libdir}/libkwnn.la
%{_includedir}/kwnn

%files -n kWnn-static
%defattr(644,root,root,755)
%{_libdir}/libkwnn.a
