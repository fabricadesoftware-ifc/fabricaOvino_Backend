export default {
  mode: "universal",
  /*
   ** Headers of the page
   */
  head: {
    title: "Ovinos - NEPPA",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "Ovinos - NEPPA" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: "#fff" },
  /*
   ** Global CSS
   */
  css: ["~/assets/css/style.scss", "@mdi/font/css/materialdesignicons.css"],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: ["~/plugins/axios"],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://buefy.github.io/#/documentation
    "@nuxtjs/style-resources",
    "@nuxtjs/toast",
    "@nuxtjs/axios",
    "nuxt-i18n",
    ["nuxt-buefy", { css: false, materialDesignIcons: true }],
  ],

  styleResources: { scss: ["~/assets/css/style.scss"] },

  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {},
  },

  toast: {
    position: "top-center",
    iconPack: "fontawesome",
    duration: 3000,
    register: [
      // Register custom toasts
      {
        name: "defaultSuccess",
        message: "Operação realizada com sucesso",
        options: {
          type: "success",
          icon: "check",
        },
      },
      {
        name: "defaultError",
        message: (payload) => (!payload.msg ? "Oops.. Erro inesperado" : payload.msg),
        options: {
          type: "error",
          icon: "times",
        },
      },
    ],
  },

  axios: {
    proxy: true,
  },

  proxy: {
    "/api/": "http://localhost:8000/",
  },

  fontawesome: {
    imports: [
      {
        set: "@fortawesome/free-solid-svg-icons",
        icons: ["fas"],
      },
    ],
  },

  i18n: {
    locales: [
      {
        code: "en",
        iso: "en-US",
        name: "English",
        file: "en/translations.json",
      },
      {
        code: "pt",
        iso: "pt-BR",
        name: "Português",
        file: "pt/translations.json",
      },
    ],
    defaultLocale: "pt",
    vueI18n: {
      fallbackLocale: "pt",
      silentTranslationWarn: true,
      silentFallbackWarn: false,
    },
    strategy: "prefix",
    lazy: true,
    langDir: "locales/",
    rootRedirect: "pt",
    seo: false,
  },
};
