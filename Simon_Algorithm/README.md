\documentclass[a4paper]{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{braket}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{colortbl}
\usepackage{bm}

%\usepackage{quantikz}
\usepackage{tikz}
\usetikzlibrary{quantikz}
\usepackage{circuitikz}
\usepackage{tikz}
\usetikzlibrary{circuits.logic.US}
%%%%%%%%%%%%%% these two packages are for colored box %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{xcolor}
\usepackage{mdframed}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{multirow} % for plotting multirow
\usepackage{adjustbox} % For adjustbox environment


\usepackage{geometry}

% Set custom margins
\geometry{left=2cm, right=2cm}
\newcommand{\verticaltext}[1]{\rotatebox[origin=c]{90}{#1}}


\title{Iterative Quantum Square Root Algorithm}
\author{Emad Rezaei Fard Boosari, Magdalena Stobinska}
\date{\today}

\begin{document}
\maketitle
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Introduction}



\begin{center}
    \begin{quantikz}
\lstick{$\ket{ctrl=1}$} &\qwbundle{1}    &\qw &\gate[5]{U_{\sqrt{\quad}}} &\qw          &      \\            
\lstick{$\ket{x}$}      &\qwbundle{2m}   &\qw &                           &\qw          &      \\            
\lstick{$\ket{y}$}      &\qwbundle{2}    &\qw &                           &\qw          &      \\
\lstick{$\ket{C_{in}}$} &\qwbundle{m}    &\qw &                           &\qw          &      \\                        
\lstick{$\ket{0}$}      &\qwbundle{4m-2} &\qw &                           &\qwbundle{m} &\rstick{$\ket{q}_m$}
    \end{quantikz}        
\end{center}

\end{document}







