<template>
  <div class="modal-card" style="width: auto">
    <header class="modal-card-head">
      <p class="modal-card-title">Login</p>
    </header>
    <section class="modal-card-body">
      <b-field label="Email">
        <b-input
          v-model="user.email"
          type="email"
          placeholder="Your email"
          required
        >
        </b-input>
      </b-field>

      <b-field label="Password">
        <b-input
          v-model="user.password"
          type="password"
          password-reveal
          placeholder="Your password"
          required
        >
        </b-input>
      </b-field>

      <!-- <b-checkbox>Remember me</b-checkbox> -->
    </section>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">
        Close
      </button>
      <button class="button is-primary" @click="signin">Login</button>
    </footer>
  </div>
</template>

<script>
// import { showError } from '@/plugins/global'

export default {
  data() {
    return {
      user: {}
    }
  },
  methods: {
    async signin() {
      try {
        await this.$auth.loginWith('local', {
          data: this.user
        })
        // this.$auth.setUserToken(response.data.access)
        // this.$auth.setToken('local', 'Bearer ' + response.data.access)
        // this.$auth.setRefreshToken('local', response.data.refresh)
        // this.$axios.setHeader('Authorization', 'Bearer ' + response.data.access)
        // this.$auth.ctx.app.$axios.setHeader(
        //   'Authorization',
        //   'Bearer ' + response.data.access
        // )
        this.$router.push('/')
        this.$parent.close()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    }
  }
}
</script>

<style></style>
