<template>
  <ValidationObserver ref="observer" v-slot="{ passes }">
    <form action>
      <div class="modal-card" style="width: auto;">
        <header class="modal-card-head">
          <p class="modal-card-title">{{ $t('components.user.changepassword.title') }}</p>
        </header>
        <section class="modal-card-body">
          <b-field :label="$t('components.user.changepassword.email')">
            {{
            email
            }}
          </b-field>

          <BInputWithValidation
            v-if="!isAdmin"
            rules="required"
            type="password"
            :label="$t('components.user.changepassword.currentPassword')"
            v-model="password.current_password"
          />

          <BInputWithValidation
            rules="required"
            type="password"
            :label="$t('components.user.changepassword.newPassword')"
            vid="newPassword"
            v-model="password.new_password"
          />

          <BInputWithValidation
            rules="required|confirmed:newPassword"
            name="Password"
            type="password"
            :label="$t('components.user.changepassword.confirmPassword')"
            v-model="password.confirm_password"
          />
        </section>
        <footer class="modal-card-foot">
          <button
            class="button"
            type="button"
            @click="$parent.close()"
          >{{ $t('components.user.changepassword.cancel') }}</button>
          <button
            class="button is-primary"
            @click.prevent="updatePassword"
          >{{ $t('components.user.changepassword.title') }}</button>
        </footer>
      </div>
    </form>
  </ValidationObserver>
</template>

<script>
import { ValidationObserver, ValidationProvider } from 'vee-validate'
import BInputWithValidation from '@/components/templates/BInputWithValidation'
import { showError } from '@/plugins/global'

export default {
  components: { BInputWithValidation, ValidationObserver, ValidationProvider },
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
        current_password: '',
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
