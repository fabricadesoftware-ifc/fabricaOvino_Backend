<template>
  <!-- <div class="tile is-ancestor">
    <div class="tile is-parent i-12">
      <div class="tile is-child"> -->
  <b-navbar class="is-primary">
    <template v-slot:brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <img
          src="~/assets/logo.png"
          alt="Ovinos-Logo"
          width="112"
          height="28"
        />
      </b-navbar-item>
    </template>
    <!-- <template slot="start">
            <b-navbar-item href="#">Home</b-navbar-item>
            <b-navbar-item href="#">Documentation</b-navbar-item>
            <b-navbar-dropdown label="Info">
              <b-navbar-item href="#">About</b-navbar-item>
              <b-navbar-item href="#">Contact</b-navbar-item>
            </b-navbar-dropdown>
          </template>-->

    <template v-slot:end>
      <nuxt-link
        v-for="locale in otherLanguages"
        :key="locale.code"
        class="language-flags"
        :to="switchLocalePath(locale.code)"
      >
        <country-flag :country="locale.flag" size="normal" />
      </nuxt-link>
      <UserDropdown v-if="loggedIn" />
    </template>
  </b-navbar>
  <!-- </div>
    </div>
  </div> -->
</template>

<script>
import { mapState } from 'vuex'

import CountryFlag from 'vue-country-flag'
import UserDropdown from './UserDropdown'

export default {
  components: { CountryFlag, UserDropdown },
  data: function () {
    return {
      hideUserDropdown: false
    }
  },
  computed: {
    ...mapState('auth', ['loggedIn']),
    otherLanguages() {
      let currentLang = this.$i18n.locale
      var langs = this.$i18n.locales.filter(function (lang) {
        return lang.code !== currentLang
      })
      return langs
    }
  }
  // methods: {
  //   changeLanguage(newLang) {
  //     this.$axios.setHeader('Accept-Language', newLang)
  //     this.switchLocalePath(newLang)
  //   }
  // }
}
</script>

<style>
.language-flags {
  display: flex;
  align-items: center;
  background-color: cornsilk;
}
</style>
