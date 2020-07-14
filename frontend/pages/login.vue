<template>
  <div class="auth-content">
    <div class="auth-modal">
      <img src="~/assets/logo.png" width="200" alt="Logo" />
      <hr />
      <div class="auth-title">
        {{ showSignup ? $t('pages.login.signup') : $t('pages.login.signin') }}
      </div>
      <div class="auth-form">
        <b-field>
          <b-input
            v-if="showSignup"
            v-model="user.name"
            icon="face"
            type="text "
            :placeholder="$t('pages.login.name.placeholder')"
          />
        </b-field>
        <b-field>
          <b-input
            v-model="user.email"
            type="email"
            icon="email"
            :placeholder="$t('pages.login.email.placeholder')"
          />
        </b-field>
        <b-field>
          <b-input
            v-model="user.password"
            icon="textbox-password"
            type="password"
            :placeholder="$t('pages.login.password.placeholder')"
          />
        </b-field>
        <b-field>
          <b-input
            v-if="showSignup"
            v-model="user.confirmPassword"
            icon="textbox-password"
            type="password"
            :placeholder="$t('pages.login.confirmPassword.placeholder')"
          />
        </b-field>
        <b-button v-if="showSignup" class="is-warning" @click="signup">{{
          $t('pages.login.signup')
        }}</b-button>
        <b-button v-if="!showSignup" class="is-primary" @click="signin">{{
          $t('pages.login.signin')
        }}</b-button>
      </div>

      <a href="#" @click.prevent="showSignup = !showSignup">
        <span v-if="showSignup">{{ $t('pages.login.withRegister') }}</span>
        <span v-else>{{ $t('pages.login.withoutRegister') }}</span>
      </a>
    </div>
  </div>
</template>

<script>
import { showError } from '@/plugins/global'
export default {
  auth: false,

  data: function () {
    return {
      showSignup: false,
      user: {}
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

<style>
.auth-content {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-modal {
  background-color: azure;
  width: 550px;
  padding: 35px;
  box-shadow: 0 12px 15px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.auth-modal img {
  background-color: #19a061;
}

.auth-modal .auth-form {
  display: flex;
  flex-direction: column;
  width: 80%;
  padding: 5px;
}

.auth-title {
  font-size: 1.4rem;
  font-weight: 400;
  margin-top: 10px;
  margin-bottom: 15px;
}

.auth-modal a {
  margin-top: 35px;
}
</style>
