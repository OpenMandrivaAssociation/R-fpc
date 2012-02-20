%bcond_without bootstrap
%global packname  fpc
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0_3
Release:          1
Summary:          Flexible procedures for clustering
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-3.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-MASS R-cluster R-mclust R-flexmix 
%if %{with bootstrap}
Requires:         R-prabclus R-class R-diptest R-mvtnorm 
%else
Requires:         R-trimcluster R-prabclus R-class R-diptest R-mvtnorm 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-cluster R-mclust R-flexmix
%if %{with bootstrap}
BuildRequires:    R-prabclus R-class R-diptest R-mvtnorm 
%else
BuildRequires:    R-trimcluster R-prabclus R-class R-diptest R-mvtnorm 
%endif

%description
Various methods for clustering and cluster validation. Fixed point
clustering. Linear regression clustering. Clustering by merging Gaussian
mixture components. Symmetric and asymmetric discriminant projections for
visualisation of the separation of groupings. Cluster validation
statistics for distance based clustering including corrected Rand index.
Clusterwise cluster stability assessment. Methods for estimation of the
number of clusters: Calinski-Harabasz, Tibshirani and Walther's prediction
strength. Gaussian/multinomial mixture fitting for mixed
continuous/categorical variables. Veriablewise statistics for cluster
interpretation. DBSCAN clustering. Interface functions for many clustering
methods implemented in R, including estimating the number of clusters with
kmeans, pam and clara. Modality diagnosis for Gaussian mixtures. Note that
the use of the package mclust (called by function prabclust) is protected
by a special license, see
http://www.stat.washington.edu/mclust/license.txt. For an overview see

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
