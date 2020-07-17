<template>
  <nav v-show="isNavBarVisible" id="navbar-main" class="navbar is-fixed-top">
    <div class="navbar-brand">
      <a
        class="navbar-item is-hidden-desktop"
        @click.prevent="menuToggleMobile"
      >
        <b-icon :icon="menuToggleMobileIcon" />
      </a>
      <div class="navbar-item has-control no-left-space-touch">
        <div class="control">
          <input class="input" placeholder="Search everywhere..." />
        </div>
      </div>
    </div>
    <div class="navbar-brand is-right">
      <a
        class="navbar-item navbar-item-menu-toggle is-hidden-desktop"
        @click.prevent="menuNavBarToggle"
      >
        <b-icon :icon="menuNavBarToggleIcon" custom-size="default" />
      </a>
    </div>
    <div
      class="navbar-menu fadeIn animated faster"
      :class="{ 'is-active': isMenuNavBarActive }"
    >
      <div v-if="loggedIn" class="navbar-end">
        <!-- <nav-bar-menu class="has-divider">
          <b-icon icon="menu" custom-size="default" />
          <span>Sample Menu</span>
          <template v-slot:dropdown>
            <div class="navbar-dropdown">
              <router-link
                to="/profile"
                class="navbar-item"
                exact-active-class="is-active"
              >
                <b-icon icon="account" custom-size="default" />
                <span>My Profile</span>
              </router-link>
              <a class="navbar-item">
                <b-icon icon="settings" custom-size="default" />
                <span>Settings</span>
              </a>
              <a class="navbar-item">
                <b-icon icon="email" custom-size="default" />
                <span>Messages</span>
              </a>
              <hr class="navbar-divider" />
              <a class="navbar-item">
                <b-icon icon="logout" custom-size="default" />
                <span>Log Out</span>
              </a>
            </div>
          </template>
        </nav-bar-menu> -->
        <nav-bar-menu class="has-divider has-user-avatar">
          <user-avatar />
          <div class="is-user-name">
            <span>{{ user.name }}</span>
          </div>

          <template v-slot:dropdown>
            <div class="navbar-dropdown">
              <nuxt-link
                :to="localePath('me')"
                class="navbar-item"
                exact-active-class="is-active"
              >
                <b-icon icon="account" custom-size="default" />
                <span>My Profile</span>
              </nuxt-link>
              <a class="navbar-item">
                <b-icon icon="settings" custom-size="default"></b-icon>
                <span>Settings</span>
              </a>
              <a class="navbar-item">
                <b-icon icon="email" custom-size="default"></b-icon>
                <span>Messages</span>
              </a>
              <hr class="navbar-divider" />
              <a class="navbar-item">
                <b-icon icon="logout" custom-size="default"></b-icon>
                <span>Log Out</span>
              </a>
            </div>
          </template>
        </nav-bar-menu>
        <a
          href="https://fabricadesoftware.ifc.edu.br"
          target="_blank"
          class="navbar-item has-divider is-desktop-icon-only"
          title="About"
        >
          <b-icon icon="help-circle-outline" custom-size="default" />
          <span>About</span>
        </a>
        <a
          class="navbar-item is-desktop-icon-only"
          title="Log out"
          @click="logout"
        >
          <b-icon icon="logout" custom-size="default" />
          <span>Log out</span>
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'
import NavBarMenu from '@/components/templates/NavBarMenu'
import UserAvatar from '@/components/templates/UserAvatar'

export default {
  name: 'NavBar',
  components: {
    UserAvatar,
    NavBarMenu
  },
  data() {
    return {
      isMenuNavBarActive: false
    }
  },
  computed: {
    ...mapState('ui', ['isNavBarVisible', 'isAsideMobileExpanded']),
    ...mapState('auth', ['loggedIn', 'user']),
    menuNavBarToggleIcon() {
      return this.isMenuNavBarActive ? 'close' : 'dots-vertical'
    },
    menuToggleMobileIcon() {
      return this.isAsideMobileExpanded ? 'backburger' : 'forwardburger'
    }
  },
  methods: {
    menuToggleMobile() {
      this.$store.commit('asideMobileStateToggle')
    },
    menuNavBarToggle() {
      this.isMenuNavBarActive = !this.isMenuNavBarActive
    },
    async logout() {
      await this.$auth.logout()
      this.$buefy.snackbar.open({
        message: 'Bye',
        queue: false
      })
    }
  }
}
</script>
