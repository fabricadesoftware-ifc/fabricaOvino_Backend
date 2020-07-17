<template>
  <div class="admin">
    <title-bar :title-stack="titleStack" />
    <hero-bar>
      {{ $t('pages.admin.title') }}
      <template v-slot:right>
        <router-link to="/" class="button">
          Dashboard
        </router-link>
      </template>
    </hero-bar>

    <card-component>
      <b-tabs>
        <b-tab-item :label="$t('pages.admin.tabs.users')">
          <UserAdmin />
        </b-tab-item>

        <b-tab-item :label="$t('pages.admin.tabs.groups')">
          <GroupAdmin />
        </b-tab-item>
      </b-tabs>
    </card-component>
  </div>
</template>

<script>
import TitleBar from '@/components/templates/TitleBar'
import HeroBar from '@/components/templates/HeroBar'
import CardComponent from '@/components/templates/CardComponent'
import UserAdmin from '@/components/admin/UserAdmin'
import GroupAdmin from '@/components/admin/GroupAdmin'
export default {
  components: { TitleBar, HeroBar, CardComponent, UserAdmin, GroupAdmin },
  computed: {
    titleStack() {
      return ['Admin', this.$t('pages.admin.subtitle')]
    }
  }
}
</script>

<style></style>
