<template>
  <div class="is-user-avatar">
    <Gravatar :email="user.email" alt="user" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Gravatar from 'vue-gravatar'

export default {
  components: { Gravatar },
  props: {
    avatar: {
      type: String,
      default: null
    }
  },
  computed: {
    ...mapState('auth', ['loggedIn', 'user'])
  }
}
</script>
