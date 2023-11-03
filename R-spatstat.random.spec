#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-spatstat.random
Version  : 3.2.1
Release  : 21
URL      : https://cran.r-project.org/src/contrib/spatstat.random_3.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.random_3.2-1.tar.gz
Summary  : Random Generation Functionality for the 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.random-lib = %{version}-%{release}
Requires: R-spatstat.data
Requires: R-spatstat.geom
Requires: R-spatstat.utils
BuildRequires : R-spatstat.data
BuildRequires : R-spatstat.geom
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
Generates random spatial patterns of points according to many simple rules (complete spatial randomness,
	     Poisson, binomial, random grid, systematic, cell), randomised alteration of patterns
	     (thinning, random shift, jittering),  simulated realisations of random point processes including
	     simple sequential inhibition, Matern inhibition models, Neyman-Scott cluster processes
	     (using direct, Brix-Kendall, or hybrid algorithms),
	     log-Gaussian Cox processes, product shot noise cluster processes
	     and Gibbs point processes (using Metropolis-Hastings birth-death-shift algorithm,
	     alternating Gibbs sampler, or coupling-from-the-past perfect simulation).
	     Also generates random spatial patterns of line segments,
	     random tessellations, and random images (random noise, random mosaics).
	     Excludes random generation on a linear network,
	     which is covered by the separate package 'spatstat.linnet'.

%package lib
Summary: lib components for the R-spatstat.random package.
Group: Libraries

%description lib
lib components for the R-spatstat.random package.


%prep
%setup -q -n spatstat.random
pushd ..
cp -a spatstat.random buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698074179

%install
export SOURCE_DATE_EPOCH=1698074179
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.random/CITATION
/usr/lib64/R/library/spatstat.random/DESCRIPTION
/usr/lib64/R/library/spatstat.random/INDEX
/usr/lib64/R/library/spatstat.random/Meta/Rd.rds
/usr/lib64/R/library/spatstat.random/Meta/features.rds
/usr/lib64/R/library/spatstat.random/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.random/Meta/links.rds
/usr/lib64/R/library/spatstat.random/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.random/Meta/package.rds
/usr/lib64/R/library/spatstat.random/NAMESPACE
/usr/lib64/R/library/spatstat.random/NEWS
/usr/lib64/R/library/spatstat.random/R/spatstat.random
/usr/lib64/R/library/spatstat.random/R/spatstat.random.rdb
/usr/lib64/R/library/spatstat.random/R/spatstat.random.rdx
/usr/lib64/R/library/spatstat.random/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.random/help/AnIndex
/usr/lib64/R/library/spatstat.random/help/aliases.rds
/usr/lib64/R/library/spatstat.random/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.random/help/paths.rds
/usr/lib64/R/library/spatstat.random/help/spatstat.random.rdb
/usr/lib64/R/library/spatstat.random/help/spatstat.random.rdx
/usr/lib64/R/library/spatstat.random/html/00Index.html
/usr/lib64/R/library/spatstat.random/html/R.css
/usr/lib64/R/library/spatstat.random/tests/RMH.R
/usr/lib64/R/library/spatstat.random/tests/Random.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.random/libs/spatstat.random.so
/usr/lib64/R/library/spatstat.random/libs/spatstat.random.so.avx2
/usr/lib64/R/library/spatstat.random/libs/spatstat.random.so.avx512
