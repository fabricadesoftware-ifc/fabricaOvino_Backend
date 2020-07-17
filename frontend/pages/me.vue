<template>
  <section>
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.me.subtitle') }}
      <template v-slot:right>
        <div class="buttons">
          <b-button @click="editUser(user)">Editar Perfil</b-button>
          <b-button type="is-warning" @click="isChangingPassword = true"
            >Alterar Senha</b-button
          >
        </div>
      </template>
    </hero-bar>
    <card-component>
      <avatar :email="user.email" />
      <personal-info :user="user" />
    </card-component>
    <card-component>
      <div class="buttons">
        <b-button @click="editUser(user)">Editar Perfil</b-button>
      </div>
    </card-component>
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
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'

export default {
  components: {
    Avatar,
    ChangePassword,
    TitleBar,
    HeroBar,
    CardComponent,
    PersonalInfo
  },
  data() {
    return {
      isChangingPassword: false
    }
  },
  computed: {
    ...mapState('auth', ['loggedIn', 'user']),
    titleStack() {
      return ['Admin', this.$t('pages.me.title')]
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
