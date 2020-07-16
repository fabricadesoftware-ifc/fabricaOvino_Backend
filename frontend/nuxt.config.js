export default {
  mode: 'universal',
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['~/assets/css/style.scss', '@mdi/font/css/materialdesignicons.css'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['~/plugins/axios', '~/plugins/vee-validate.js'],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://buefy.github.io/#/documentation
    '@nuxtjs/style-resources',
    '@nuxtjs/toast',
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    'nuxt-i18n',
    ['nuxt-buefy', { css: false, materialDesignIcons: true }]
  ],

  styleResources: { scss: ['~/assets/css/style.scss'] },

  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    transpile: ['vee-validate/dist/rules'],
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },

  // pages: {
  //   login: {
  //     en: "/login",
  //     pt: "/login",
  //   },
  // },

  auth: {
    localStorage: false,
    // cookie: {
    //   options: {
    //     expires: 7
    //   }
    // },
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/api/v1/token/',
            method: 'post',
            propertyName: 'access',
            altProperty: 'refresh'
          },
          // refresh: {
          //   url: '/api/v1/token_refresh',
          //   method: 'post',
          //   propertyName: ''
          // },
          logout: {},
          // user: false,
          user: {
            url: '/api/v1/users/logged/',
            method: 'get',
            propertyName: false
          }
        }
      }
    },
    resetOnError: true,
    redirect: {
      login: '/login',
      logout: '/logout'
    },
    plugins: [
      '@/plugins/auth-lang-redirect',
      { src: '@/plugins/auth.js', mode: 'client' }
    ]
  },

  router: {
    middleware: [
      // Needed for redirection to the login page when not authenticated
      'auth'
      // 'lang'
    ]
  },

  toast: {
    position: 'top-center',
    iconPack: 'fontawesome',
    duration: 3000,
    register: [
      // Register custom toasts
      {
        name: 'defaultSuccess',
        message: 'Operação realizada com sucesso',
        options: {
          type: 'success',
          icon: 'check'
        }
      },
      {
        name: 'defaultError',
        message: payload =>
          !payload.msg ? 'Oops.. Erro inesperado' : payload.msg,
        options: {
          type: 'error',
          icon: 'times'
        }
      }
    ]
  },

  axios: {
    baseURL: 'http://localhost:8000'
  },

  // proxy: {
  //   '/api/': 'http://localhost:8000/'
  // },

  fontawesome: {
    imports: [
      {
        set: '@fortawesome/free-solid-svg-icons',
        icons: ['fas']
      }
    ]
  },

  i18n: {
    locales: [
      {
        code: 'en',
        iso: 'en',
        name: 'English',
        file: 'en/translations.json',
        flag: 'us'
      },
      {
        code: 'pt',
        iso: 'pt-br',
        name: 'Português',
        file: 'pt/translations.json',
        flag: 'br'
      }
    ],
    defaultLocale: 'pt',
    vueI18n: {
      fallbackLocale: 'pt',
      silentTranslationWarn: true,
      silentFallbackWarn: false
    },
    strategy: 'prefix',
    lazy: true,
    langDir: 'locales/',
    rootRedirect: 'pt',
    seo: true
    // onLanguageSwitched: ctx => {
    //   console.log($axios + ctx)
    // }
  }
  /*
   ** Headers of the page
   */
  // head: {
  //   title: 'Ovinos - NEPPA',
  //   meta: [
  //     { charset: 'utf-8' },
  //     { name: 'viewport', content: 'width=device-width, initial-scale=1' },
  //     { hid: 'description', name: 'description', content: 'Ovinos - NEPPA' }
  //   ],
  //   link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  // }
}
