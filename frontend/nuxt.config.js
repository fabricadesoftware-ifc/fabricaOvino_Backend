export default {
  mode: 'universal',
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['~/assets/scss/main.scss', '@mdi/font/css/materialdesignicons.css'],
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
    '@nuxtjs/auth-next',
    'nuxt-i18n',
    ['nuxt-buefy', { css: false, materialDesignIcons: true }]
  ],

  styleResources: { scss: ['~/assets/scss/main.scss'] },

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

  auth: {
    localStorage: false,
    cookie: {
      options: {
        secure: process.env.NODE_ENV === 'production'
      }
    },

    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access'
        },
        refreshToken: {
          property: 'refresh',
          data: 'refresh',
          maxAge: 60 * 60 * 24 * 30
        },
        user: {
          property: 'user'
        },
        endpoints: {
          login: {
            url: '/api/v1/token/',
            method: 'post',
            propertyName: 'access',
            altProperty: 'refresh'
          },
          refresh: {
            url: '/api/v1/refresh_token/',
            method: 'post'
            //   propertyName: ''
          },
          logout: {},
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
      '@/plugins/auth-lang-redirect'
      // { src: '@/plugins/auth.js', mode: 'client' }
    ]
  },

  router: {
    middleware: ['auth']
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
  },
  /*
   ** Headers of the page
   */
  head: {
    title: 'Ovinos - NEPPA',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Ovinos - NEPPA' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'dns-prefetch', href: 'https://fonts.gstatic.com' },
      {
        href: 'https://fonts.googleapis.com/css2?family=Nunito&display=swap',
        rel: 'stylesheet'
      }
    ],
    htmlAttrs: {
      class: [
        'has-aside-left',
        'has-aside-mobile-transition',
        'has-navbar-fixed-top',
        'has-aside-expanded'
      ]
    }
  }
}
