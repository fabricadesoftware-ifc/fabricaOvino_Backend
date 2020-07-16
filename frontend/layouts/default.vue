<template>
  <div>
    <HeaderUI />
    <div class="tile is-ancestor">
      <div class="tile is-parent is-2">
        <MenuUI />
      </div>
      <div class="tile is-parent">
        <div class="tile is-child is-11">
          <nuxt />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderUI from '@/components/ui/HeaderUI'
import MenuUI from '@/components/ui/MenuUI'
export default {
  components: { HeaderUI, MenuUI },
  head() {
    const i18nSeo = this.$nuxtI18nSeo()
    const locale = this.$i18n.locale
    const language = this.$i18n.locales.find(function (lang) {
      return lang.code == locale
    })
    this.$axios.setHeader('Accept-Language', language.iso)
    return {
      htmlAttrs: {
        // lang: language.iso,
        ...i18nSeo.htmlAttrs
      },
      title: 'Ovinos - NEPPA - Fábrica',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: 'Ovinos - NEPPA' },
        ...i18nSeo.meta
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        ...i18nSeo.link
      ]
    }
  }
}
</script>

<style>
* {
  font-family: 'Lato', sans-serif;
}
body {
  margin: 0;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  height: 100vh;
  /* display: grid;
  grid-template-rows: 60px 1fr 40px;
  grid-template-columns: 300px 1fr;
  grid-template-areas:
    "header header"
    "menu content"
    "menu footer"; */
}
</style>
