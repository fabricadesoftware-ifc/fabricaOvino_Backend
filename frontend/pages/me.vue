<template>
  <section>
    <page-title
      icon="face"
      :main="$t('pages.me.title')"
      :sub="$t('pages.me.subtitle')"
    />

    {{ user }}
    <b-button @click="editUser(user)">Editar Perfil</b-button>
    <b-button @click="isChangingPassword = true">Alterar Senha</b-button>
    <avatar :email="user.email" />
    <personal-info :user="user" />

    <b-button @click="editUser(user)">Editar Perfil</b-button>

    <b-modal
      :active.sync="isChangingPassword"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
      aria-modal
    >
      <change-password :id="user.id" :email="user.email"></change-password>
    </b-modal>
  </section>
</template>

<script>
import { mapState } from 'vuex'
import Avatar from '@/components/user/Avatar'
import ChangePassword from '@/components/user/ChangePassword'
import PersonalInfo from '@/components/user/PersonalInfo'
import PageTitle from '@/components/templates/PageTitle'

export default {
  components: { Avatar, ChangePassword, PageTitle, PersonalInfo },
  computed: {
    ...mapState('auth', ['loggedIn', 'user'])
  },
  data() {
    return {
      isChangingPassword: false
    }
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
