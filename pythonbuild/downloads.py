# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

DOWNLOADS = {
    # 6.0.19 is the last version licensed under the Sleepycat license.
    'bdb': {
        'url': 'https://ftp.tw.freebsd.org/distfiles/bdb/db-6.0.19.tar.gz',
        'size': 36541923,
        'sha256': '2917c28f60903908c2ca4587ded1363b812c4e830a5326aaa77c9879d13ae18e',
        'version': '6.0.19',
        'library_names': ['db'],
        'licenses': ['Sleepycat'],
        'license_file': 'LICENSE.bdb.txt',
    },
    'binutils': {
        'url': 'ftp://ftp.gnu.org/gnu/binutils/binutils-2.32.tar.xz',
        'size': 20774880,
        'sha256': '0ab6c55dd86a92ed561972ba15b9b70a8b9f75557f896446c82e8b36e473ee04',
        'version': '2.32',
    },
    'bzip2': {
        'url': 'https://ftp.sunet.se/mirror/archive/ftp.sunet.se/pub/Linux/distributions/bifrost/download/src/bzip2-1.0.6.tar.gz',
        'size': 782025,
        'sha256': 'a2848f34fcd5d6cf47def00461fcb528a0484d8edef8208d6d2e2909dc61d9cd',
        'version': '1.0.6',
        'library_names': ['bz2'],
        'licenses': ['bzip2-1.0.6'],
        'license_file': 'LICENSE.bzip2.txt',
    },
    'clang': {
        'url': 'http://releases.llvm.org/8.0.0/cfe-8.0.0.src.tar.xz',
        'size': 12868468,
        'sha256': '084c115aab0084e63b23eee8c233abb6739c399e29966eaeccfc6e088e0b736b',
        'version': '8.0.0',
    },
    'clang-6': {
        'url': 'http://releases.llvm.org/6.0.1/cfe-6.0.1.src.tar.xz',
        'size': 11905772,
        'sha256': '7c243f1485bddfdfedada3cd402ff4792ea82362ff91fbdac2dae67c6026b667',
        'version': '6.0.1',
    },
    'clang-compiler-rt': {
        'url': 'http://releases.llvm.org/8.0.0/compiler-rt-8.0.0.src.tar.xz',
        'size': 1903020,
        'sha256': 'b435c7474f459e71b2831f1a4e3f1d21203cb9c0172e94e9d9b69f50354f21b1',
        'version': '8.0.0',
    },
    'clang-compiler-rt-6': {
        'url': 'http://releases.llvm.org/6.0.1/compiler-rt-6.0.1.src.tar.xz',
        'size': 1686820,
        'sha256': 'f4cd1e15e7d5cb708f9931d4844524e4904867240c306b06a4287b22ac1c99b9',
        'version': '6.0.1',
    },
    'cmake-linux-bin': {
        'url': 'https://github.com/Kitware/CMake/releases/download/v3.13.0/cmake-3.13.0-Linux-x86_64.tar.gz',
        'size': 38391207,
        'sha256': '1c6612f3c6dd62959ceaa96c4b64ba7785132de0b9cbc719eea6fe1365cc8d94',
        'version': '3.13.0',
    },
    'cmake-macos-bin': {
        'url': 'https://github.com/Kitware/CMake/releases/download/v3.13.2/cmake-3.13.2-Darwin-x86_64.tar.gz',
        'size': 32049991,
        'sha256': '747659e5adbf422d9202f053a97439bcd61616420600cc89d07cbd94213d382d',
        'version': '3.13.2',
    },
    'cpython-3.7': {
        'url': 'https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz',
        'size': 17131432,
        'sha256': 'fb799134b868199930b75f26678f18932214042639cd52b16da7fd134cd9b13f',
        'version': '3.7.4',
        'licenses': ['Python-2.0', 'CNRI-Python'],
        'license_file': 'LICENSE.cpython.txt',
    },
    'gcc': {
        'url': 'https://ftp.gnu.org/gnu/gcc/gcc-9.1.0/gcc-9.1.0.tar.xz',
        'size': 70546856,
        'sha256': '79a66834e96a6050d8fe78db2c3b32fb285b230b855d0a66288235bc04b327a0',
        'version': '9.1.0',
    },
    'gdbm': {
        'url': 'ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.18.1.tar.gz',
        'size': 941863,
        'sha256': '86e613527e5dba544e73208f42b78b7c022d4fa5a6d5498bf18c8d6f745b91dc',
        'version': '1.18.1',
        'library_names': ['gdbm'],
        'licenses': ['GPL-3.0-or-later'],
        'license_file': 'LICENSE.gdbm.txt',
    },
    'gmp': {
        'url': 'https://ftp.gnu.org/gnu/gmp/gmp-6.1.2.tar.xz',
        'size': 1946336,
        'sha256': '87b565e89a9a684fe4ebeeddb8399dce2599f9c9049854ca8c0dfbdea0e21912',
        'version': '6.1.2',
    },
    'isl': {
        'url': 'ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-0.18.tar.bz2',
        'size': 1658291,
        'sha256': '6b8b0fd7f81d0a957beb3679c81bbb34ccc7568d5682844d8924424a0dadcb1b',
        'version': '0.18',
    },
    'libc++': {
        'url': 'http://releases.llvm.org/8.0.0/libcxx-8.0.0.src.tar.xz',
        'size': 1752308,
        'sha256': 'c2902675e7c84324fb2c1e45489220f250ede016cc3117186785d9dc291f9de2',
        'version': '8.0.0',
    },
    'libc++-6': {
        'url': 'http://releases.llvm.org/6.0.1/libcxx-6.0.1.src.tar.xz',
        'size': 1552328,
        'sha256': '7654fbc810a03860e6f01a54c2297a0b9efb04c0b9aa0409251d9bdb3726fc67',
        'version': '6.0.1',
    },
    'libc++abi': {
        'url': 'http://releases.llvm.org/8.0.0/libcxxabi-8.0.0.src.tar.xz',
        'size': 539040,
        'sha256': 'c2d6de9629f7c072ac20ada776374e9e3168142f20a46cdb9d6df973922b07cd',
        'version': '8.0.0',
    },
    'libc++abi-6': {
        'url': 'http://releases.llvm.org/6.0.1/libcxxabi-6.0.1.src.tar.xz',
        'size': 528356,
        'sha256': '209f2ec244a8945c891f722e9eda7c54a5a7048401abd62c62199f3064db385f',
        'version': '6.0.1',
    },
    'libedit': {
        'url': 'https://www.thrysoee.dk/editline/libedit-20181209-3.1.tar.gz',
        'size': 521931,
        'sha256': '2811d70c0b000f2ca91b7cb1a37203134441743c4fcc9c37b0b687f328611064',
        'version': '20181209-3.1',
        'library_names': ['edit'],
        'licenses': ['BSD-3-Clause'],
        'license_file': 'LICENSE.libedit.txt',
    },
    'libffi': {
        'url': 'ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz',
        'size': 940837,
        'sha256': 'd06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37',
        'version': '3.2.1',
        'library_names': ['ffi'],
        'licenses': ['MIT'],
        'license_file': 'LICENSE.libffi.txt',
    },
    'libressl': {
        'url': 'https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.9.2.tar.gz',
        'size': 3607549,
        'sha256': 'c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4',
        'version': '2.9.2',
        'library_names': ['crypto', 'ssl'],
        'licenses': ['OpenSSL'],
        'license_file': 'LICENSE.libressl.txt',
    },
    'libx11': {
        'url': 'https://www.x.org/releases/X11R7.7/src/lib/libX11-1.5.0.tar.gz',
        'size': 3073820,
        'sha256': '2ddc05170baf70dd650ee6108c5882eb657cafaf61a5b5261badb26703122518',
    },
    'lld': {
        'url': 'http://releases.llvm.org/8.0.0/lld-8.0.0.src.tar.xz',
        'size': 999864,
        'sha256': '9caec8ec922e32ffa130f0fb08e4c5a242d7e68ce757631e425e9eba2e1a6e37',
        'version': '8.0.0',
    },
    'lld-6': {
        'url': 'http://releases.llvm.org/6.0.1/lld-6.0.1.src.tar.xz',
        'size': 787804,
        'sha256': 'e706745806921cea5c45700e13ebe16d834b5e3c0b7ad83bf6da1f28b0634e11',
        'version': '6.0.1',
    },
    'llvm': {
        'url': 'http://releases.llvm.org/8.0.0/llvm-8.0.0.src.tar.xz',
        'size': 30503732,
        'sha256': '8872be1b12c61450cacc82b3d153eab02be2546ef34fa3580ed14137bb26224c',
        'version': '8.0.0',
    },
    'llvm-6': {
        'url': 'http://releases.llvm.org/6.0.1/llvm-6.0.1.src.tar.xz',
        'size': 25306628,
        'sha256': 'b6d6c324f9c71494c0ccaf3dac1f16236d970002b42bb24a6c9e1634f7d0f4e2',
        'version': '6.0.1',
    },
    'mpc': {
        'url': 'http://www.multiprecision.org/downloads/mpc-1.0.3.tar.gz',
        'size': 669925,
        'sha256': '617decc6ea09889fb08ede330917a00b16809b8db88c29c31bfbb49cbf88ecc3',
        'version': '1.0.3',
    },
    'mpfr': {
        'url': 'https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.6.tar.xz',
        'size': 1133672,
        'sha256': '7a62ac1a04408614fccdc506e4844b10cf0ad2c2b1677097f8f35d3a1344a950',
        'version': '3.1.6',
    },
    'musl': {
        'url': 'https://www.musl-libc.org/releases/musl-1.1.22.tar.gz',
        'size': 987296,
        'sha256': '8b0941a48d2f980fd7036cfbd24aa1d414f03d9a0652ecbd5ec5c7ff1bee29e3',
        'version': '1.1.22',
    },
    'ncurses': {
        'url': 'https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.1.tar.gz',
        'size': 3365395,
        'sha256': 'aa057eeeb4a14d470101eff4597d5833dcef5965331be3528c08d99cebaa0d17',
        'version': '6.1',
        'library_names': ['ncurses', 'panel'],
        'licenses': ['X11'],
        'license_file': 'LICENSE.ncurses.txt',
    },
    'ninja-linux-bin': {
        'url': 'https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip',
        'size': 77854,
        'sha256': 'd2fea9ff33b3ef353161ed906f260d565ca55b8ca0568fa07b1d2cab90a84a07',
        'version': '1.8.2',
    },
    'ninja-macos-bin': {
        'url': 'https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-mac.zip',
        'size': 77284,
        'sha256': '0347d55c66061652b26f48769d566761630ffde3143793b29064a57f356542cc',
        'version': '1.8.2',
    },
    'openssl': {
        'url': 'https://www.openssl.org/source/openssl-1.1.1c.tar.gz',
        'size': 8864262,
        'sha256': 'f6fb3079ad15076154eda9413fed42877d668e7069d9b87396d0804fdb3f4c90',
        'version': '1.1.1c',
        'library_names': ['crypto', 'ssl'],
        'licenses': ['OpenSSL'],
        'license_file': 'LICENSE.openssl.txt',
    },
    'nasm-windows-bin': {
        'url': 'https://github.com/python/cpython-bin-deps/archive/nasm-2.11.06.tar.gz',
        'size': 384826,
        'sha256': '8af0ae5ceed63fa8a2ded611d44cc341027a91df22aaaa071efedc81437412a5',
        'version': '2.11.06',
    },
    'pip': {
        'url': 'https://files.pythonhosted.org/packages/93/ab/f86b61bef7ab14909bd7ec3cd2178feb0a1c86d451bc9bccd5a1aedcde5f/pip-19.1.1.tar.gz',
        'size': 1334144,
        'sha256': '44d3d7d3d30a1eb65c7e5ff1173cdf8f7467850605ac7cc3707b6064bddd0958',
        'version': '19.1.1',
    },
    'readline': {
        'url': 'ftp://ftp.gnu.org/gnu/readline/readline-6.3.tar.gz',
        'size': 2468560,
        'sha256': '56ba6071b9462f980c5a72ab0023893b65ba6debb4eeb475d7a563dc65cafd43',
        'version': '6.3',
        'library_names': ['readline'],
        'licenses': ['GPL-3.0'],
        'license_file': 'LICENSE.readline.txt',
    },
    'rust': {
        'url': 'https://static.rust-lang.org/dist/rust-1.30.1-x86_64-unknown-linux-gnu.tar.gz',
        'size': 236997689,
        'sha256': 'a01a493ed8946fc1c15f63e74fc53299b26ebf705938b4d04a388a746dfdbf9e',
    },
    'setuptools': {
        'url': 'https://files.pythonhosted.org/packages/1d/64/a18a487b4391a05b9c7f938b94a16d80305bf0369c6b0b9509e86165e1d3/setuptools-41.0.1.zip',
        'size': 849016,
        'sha256': 'a222d126f5471598053c9a77f4b5d4f26eaa1f150ad6e01dcf1a42e185d05613',
        'version': '41.0.1',
    },
    'sqlite': {
        'url': 'https://www.sqlite.org/2019/sqlite-autoconf-3280000.tar.gz',
        'size': 2810415,
        'sha256': 'd61b5286f062adfce5125eaf544d495300656908e61fca143517afcc0a89b7c3',
        'version': '3280000',
        'actual_version': '3.28.0.0',
        'library_names': ['sqlite3'],
        'licenses': [],
        'license_file': 'LICENSE.sqlite.txt',
        'license_public_domain': True,
    },
    'strawberryperl': {
        'url': 'http://strawberryperl.com/download/5.28.1.1/strawberry-perl-5.28.1.1-32bit-portable.zip',
        'size': 143242779,
        'sha256': '8b15c7c9574989568254a7859e473b7d5f68a1145d2e4418036600a81b13805c',
        'version': '5.28.1.1',
    },
    'tcl': {
        'url': 'https://prdownloads.sourceforge.net/tcl/tcl8.6.9-src.tar.gz',
        'size': 10000896,
        'sha256': 'ad0cd2de2c87b9ba8086b43957a0de3eb2eb565c7159d5f53ccbba3feb915f4e',
    },
    'tk': {
        'url': 'https://prdownloads.sourceforge.net/tcl/tk8.6.9.1-src.tar.gz',
        'size': 4364603,
        'sha256': '8fcbcd958a8fd727e279f4cac00971eee2ce271dc741650b1fc33375fb74ebb4',
    },
    'tk-windows-bin': {
        'url': 'https://github.com/python/cpython-bin-deps/archive/86027ce3edda1284ae4bf6c2c580288366af4052.tar.gz',
        'size': 7162470,
        'sha256': '34400f7b76a13389a475fc1a4d6e33d5ca21dda6f6ff11b04759865814bdf3d2',
        'version': '6.6.9',
        'git_commit': '86027ce3edda1284ae4bf6c2c580288366af4052',
    },
    'uuid': {
        'url': 'https://sourceforge.net/projects/libuuid/files/libuuid-1.0.3.tar.gz',
        'size': 318256,
        'sha256': '46af3275291091009ad7f1b899de3d0cea0252737550e7919d17237997db5644',
        'version': '1.0.3',
        'library_names': ['uuid'],
        'licenses': ['BSD-3-Clause'],
        'license_file': 'LICENSE.libuuid.txt',
    },
    'xz': {
        'url': 'https://tukaani.org/xz/xz-5.2.4.tar.gz',
        'size': 1572354,
        'sha256': 'b512f3b726d3b37b6dc4c8570e137b9311e7552e8ccbab4d39d47ce5f4177145',
        'version': '5.2.4',
        'library_names': ['lzma'],
        # liblzma is in the public domain. Other parts of code have licenses. But
        # we only use liblzma.
        'licenses': [],
        'license_file': 'LICENSE.liblzma.txt',
        'license_public_domain': True,
    },
    'zlib': {
        'url': 'https://zlib.net/zlib-1.2.11.tar.gz',
        'size': 607698,
        'sha256': 'c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1',
        'version': '1.2.11',
        'library_names': ['z'],
        'licenses': ['Zlib'],
        'license_file': 'LICENSE.zlib.txt',
    },
}
