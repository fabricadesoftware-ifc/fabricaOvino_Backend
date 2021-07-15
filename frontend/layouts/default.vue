<template>
  <div>
    <nav-bar />
    <aside-menu :menu="menu" />
    <nuxt />
    <footer-bar />
  </div>
</template>

<script>
// import MenuUI from '@/components/ui/MenuUI'
import NavBar from '@/components/templates/NavBar'
import AsideMenu from '@/components/templates/AsideMenu'
import FooterBar from '@/components/templates/FooterBar'

export default {
  components: { NavBar, AsideMenu, FooterBar },
  computed: {
    menu() {
      return [
        this.$t('asideMenu.general'),
        [
          {
            to: '/',
            icon: 'desktop-mac',
            label: this.$t('asideMenu.dashboard')
          }
        ],
        this.$t('asideMenu.adminItems.title'),
        [
          {
            to: { name: 'category' },
            label: this.$t('asideMenu.adminItems.category'),
            icon: 'alpha-c-circle-outline'
          },
          {
            to: { name: 'breed' },
            label: this.$t('asideMenu.adminItems.breed'),
            icon: 'puzzle'
          },
          {
            to: { name: 'feed' },
            label: this.$t('asideMenu.adminItems.feed'),
            icon: 'silverware'
          },
          {
            label: this.$t('asideMenu.adminItems.sheep'),
            icon: 'sheep',
            to: { name: 'sheep' }
          },
          {
            label: this.$t('asideMenu.adminItems.records'),
            icon: 'view-list',
            updateMark: true,
            menu: [
              {
                label: this.$t('asideMenu.adminItems.shearing'),
                icon: 'scissors-cutting',
                to: { name: 'shearing' }
              }
            ]
          }
        ],
        this.$t('asideMenu.reproductionItems.title'),
        [
          {
            to: { name: 'lots' },
            icon: 'view-grid',
            label: this.$t('asideMenu.reproductionItems.lots')
          },
          {
            label: this.$t('asideMenu.adminItems.records'),
            icon: 'view-list',
            updateMark: true,
            menu: [
              {
                label: this.$t('asideMenu.adminItems.pregnancyDiagnosis'),
                icon: 'medical-bag',
                to: { name: 'pregnancyDiagnosis' }
              },
              {
                label: this.$t('asideMenu.adminItems.birth'),
                icon: 'lightbulb-outline',
                to: { name: 'birth' }
              }
            ]
          }
        ],
        this.$t('asideMenu.reproductionItems.restroom'),
        this.$t('asideMenu.about'),
        [
          {
            href: 'https://fabricadesoftware.ifc.edu.br',
            label: this.$t('asideMenu.about'),
            icon: 'help-circle'
          }
        ]
      ]
    }
  },
  head() {
    // const i18nSeo = this.$nuxtI18nSeo()
    const locale = this.$i18n.locale
    const language = this.$i18n.locales.find(function (lang) {
      return lang.code == locale
    })
    this.$axios.setHeader('Accept-Language', language.iso)
    //   return {
    //     htmlAttrs: {
    //       // lang: language.iso,
    //       ...i18nSeo.htmlAttrs
    //     },
    //     title: 'Ovinos - NEPPA - Fábrica',
    //     meta: [
    //       { charset: 'utf-8' },
    //       { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    //       { hid: 'description', name: 'description', content: 'Ovinos - NEPPA' },
    //       ...i18nSeo.meta
    //     ],
    //     link: [
    //       { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    //       ...i18nSeo.link
    //     ]
    //   }
  }
}
</script>

<style>
/* {
  /* font-family: 'Lato', sans-serif;
}
body {
  margin: 0;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  height: 100vh; */
/* display: grid;
  grid-template-rows: 60px 1fr 40px;
  grid-template-columns: 300px 1fr;
  grid-template-areas:
    "header header"
    "menu content"
    "menu footer"; 
}*/
</style>
