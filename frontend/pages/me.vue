<template>
  <section>
    <page-title icon="face" :main="$t('pages.me.title')" :sub="$t('pages.me.subtitle')" />
    <b-button @click="editUser(user)">Editar Perfil</b-button>
    <avatar :email="user.email" />
    <personal-info :user="user" />

    <b-button @click="editUser(user)">Editar Perfil</b-button>
  </section>
</template>

<script>
import { mapState } from 'vuex'
import Avatar from '@/components/user/Avatar'
import PersonalInfo from '@/components/user/PersonalInfo'
import PageTitle from '@/components/templates/PageTitle'


export default {
  components: { Avatar, PageTitle, PersonalInfo },
  computed: {
    ...mapState('auth', ['loggedIn', 'user'])
  },
  methods: {
    editUser(user) {
      this.$router.push({
        name: `admin-user-edit___${this.$i18n.locale}`,
        params: { user }
      })
    }
  }
}
</script>

<style></style>
