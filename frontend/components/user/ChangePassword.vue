<template>
  <ValidationObserver ref="observer" v-slot="{}">
    <form action>
      <div class="modal-card" style="width: auto;">
        <header class="modal-card-head">
          <p class="modal-card-title">
            {{ $t('components.user.changepassword.title') }}
          </p>
        </header>
        <section class="modal-card-body">
          <b-field :label="$t('components.user.changepassword.email')">
            {{ email }}
          </b-field>

          <v-input
            v-if="!isAdmin"
            v-model="password.current_password"
            rules="required"
            type="password"
            :label="$t('components.user.changepassword.currentPassword')"
          />

          <v-input
            v-model="password.new_password"
            rules="required"
            type="password"
            :label="$t('components.user.changepassword.newPassword')"
            vid="newPassword"
          />

          <v-input
            v-model="password.confirm_password"
            rules="required|confirmed:newPassword"
            name="Password"
            type="password"
            :label="$t('components.user.changepassword.confirmPassword')"
          />
        </section>
        <footer class="modal-card-foot">
          <button class="button" type="button" @click="$parent.close()">
            {{ $t('components.user.changepassword.cancel') }}
          </button>
          <button class="button is-primary" @click.prevent="updatePassword">
            {{ $t('components.user.changepassword.title') }}
          </button>
        </footer>
      </div>
    </form>
  </ValidationObserver>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import VInput from '@/components/templates/VInput'

export default {
  components: { VInput, ValidationObserver },
  props: {
    id: {},
    email: {},
    isAdmin: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      password: {
        current_password: 'x',
        new_password: '',
        confirm_password: ''
      }
    }
  },
  methods: {
    updatePassword() {
      const id = this.id
      const url = `/api/v1/users/${id}/password/`
      this.$axios
        .$post(url, this.password)
        .then(() => {
          this.$toasted.global.defaultSuccess()
          this.reset()
        })
        .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(e.response.data[item])
          }
        })
    }
  }
}
</script>

<style></style>
