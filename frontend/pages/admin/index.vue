<template>
  <div class="admin">
    <PageTitle
      icon="cogs"
      :main="$t('pages.admin.title')"
      :sub="$t('pages.admin.subtitle')"
    />

    <b-tabs>
      <b-tab-item :label="$t('pages.admin.tabs.users')">
        <UserAdmin />
      </b-tab-item>

      <b-tab-item :label="$t('pages.admin.tabs.groups')">
        <GroupAdmin />
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import UserAdmin from '@/components/admin/UserAdmin'
import GroupAdmin from '@/components/admin/GroupAdmin'
export default {
  components: { PageTitle, UserAdmin, GroupAdmin }
}
</script>

<style></style>
