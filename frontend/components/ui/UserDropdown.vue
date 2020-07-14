<template>
  <b-dropdown
    position="is-bottom-left"
    append-to-body
    aria-role="menu"
    trap-focus
  >
    <template v-slot:trigger>
      <a class="user-dropdown-img navbar-item" role="button">
        <Gravatar :email="user.email" alt="user" />
        <b-icon icon="menu-down"></b-icon>
      </a>
    </template>

    <b-dropdown-item class="user-dropdown-userinfo" custom aria-role="menuitem">
      <Gravatar :email="user.email" alt="user" />
      <span class="user-name">{{ user.name }}</span>
      <span class="user-email">{{ user.email }}</span>
      <nuxt-link :to="localePath('me')" class="user-edit"
        >Editar informações</nuxt-link
      >
    </b-dropdown-item>

    <hr class="dropdown-section" />
    <b-dropdown-item
      value="home"
      aria-role="menuitem"
      @click="$router.push('/')"
    >
      <b-icon icon="home"></b-icon>Home
    </b-dropdown-item>
    <!-- <b-dropdown-item value="products" aria-role="menuitem">
        <b-icon icon="cart"></b-icon>TODO
      </b-dropdown-item>
      <b-dropdown-item value="blog" disabled aria-role="menuitem">
        <b-icon icon="book-open"></b-icon>TODO
      </b-dropdown-item> -->
    <hr class="dropdown-divider" aria-role="menuitem" />
    <b-dropdown-item @click="$router.push(localePath('admin'))">
      <b-icon icon="cogs"></b-icon>
      {{ $t('header.admin') }}
    </b-dropdown-item>
    <b-dropdown-item @click="$router.push(localePath('me'))">
      <b-icon icon="face"></b-icon>
      {{ $t('header.profile') }}
    </b-dropdown-item>
    <b-dropdown-item value="logout" aria-role="menuitem" @click="logout">
      <b-icon icon="logout"></b-icon>
      {{ $t('components.userdropdown.logout') }}
    </b-dropdown-item>
  </b-dropdown>
</template>

<script>
import { mapState } from 'vuex'
import Gravatar from 'vue-gravatar'

export default {
  components: { Gravatar },
  computed: {
    ...mapState('auth', ['loggedIn', 'user'])
  },
  methods: {
    async logout() {
      await this.$auth.logout()
    }
  }
}
</script>

<style>
.user-dropdown-userinfo {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 350px;
}

.user-dropdown-userinfo img {
  height: 100px;
  width: 100px;
  border-radius: 20px;
}

.user-dropdown-userinfo .user-name {
  font-size: 1.3rem;
  font-weight: 600;
}

.user-dropdown-userinfo .user-email {
  font-size: 1.1rem;
  font-weight: 300;
}

.user-dropdown-userinfo .user-edit {
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  padding: 5px;
  align-self: center;
  border: 1px solid gray;
  width: 70%;
  border-radius: 20px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
}

.user-dropdown-userinfo .user-edit:hover {
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  padding: 5px;
  align-self: center;
  border: 1px solid gray;
  width: 70%;
  border-radius: 20px;
  background-color: lightgray;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
}

.user-dropdown-img {
  margin: 0px 10px;
}

.user-dropdown-img > img {
  max-height: 37px;
  border-radius: 5px;
}
</style>
