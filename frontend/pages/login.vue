<template>
  <section>
    <b-modal
      :active.sync="isComponentModalActive"
      has-modal-card
      full-screen
      :can-cancel="false"
    >
      <form-login></form-login>
    </b-modal>
  </section>
</template>

<script>
import FormLogin from '@/components/FormLogin'
import { showError } from '@/plugins/global'
export default {
  auth: false,
  components: { FormLogin },

  data: function () {
    return {
      isComponentModalActive: true,
      showSignup: false,
      user: {},
      formProps: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async signin() {
      try {
        const response = await this.$auth.loginWith('local', {
          data: this.user
        })
        this.$auth.setUserToken(response.data.access)
        this.$auth.setToken('local', 'Bearer ' + response.data.access)
        this.$auth.setRefreshToken('local', response.data.refresh)
        this.$axios.setHeader('Authorization', 'Bearer ' + response.data.access)
        this.$auth.ctx.app.$axios.setHeader(
          'Authorization',
          'Bearer ' + response.data.access
        )
        this.$router.push('/')
      } catch (err) {
        showError(err)
      }

      // this.$auth.loginWith('local', { data: this.user }).then((response) => {
      //     console.log('logou')
      //     console.log(response)
      //     this.$auth.setUserToken(response.data.access)
      //     this.$router.push('/')
      //   }).catch( (err) => {
      //   showError(err)
      //   console.log(err)
      // })

      //   this.$axios.post(url, this.user)
      //     .then((res) => {
      //       this.$toasted.global.defaultSuccess();
      //       this.$store.commit("setUser", res.data);
      //       localStorage.setItem(userKey, JSON.stringify(res.data));
      //       this.$router.push({ path: "/" });

      //     })
      //     .catch(showError);

      //       async userLogin() {

      // }
    },
    signup() {}
  }

  // computed: {
  //   ...mapState(["login"]),
  // },
  // methods: {
  //   ...mapMutations({
  //     toggleShowSignup: 'login/toggleShowSignup'
  //   })
  // },
  // updated() {
  //   this.$forceUpdate();
  // },
  //   methods: {
  //     signin() {
  //       axios
  //         .post(`${baseApiUrl}/signin`, this.user)
  //         .then((res) => {
  //           this.$store.commit("setUser", res.data);
  //           localStorage.setItem(userKey, JSON.stringify(res.data));
  //           this.$router.push({ path: "/" });
  //         })
  //         .catch(showError);
  //     },
  //     signup() {
  //       axios
  //         .post(`${baseApiUrl}/signup`, this.user)
  //         .then(() => {
  //           this.$toasted.global.defaultSuccess();
  //           this.user = {};
  //           this.showSignup = false;
  //         })
  //         .catch(showError);
  //     },
  //   },
}
</script>
