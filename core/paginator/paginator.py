# -*- coding: utf-8 -*-

from drf_link_header_pagination import LinkHeaderPagination
from rest_framework.response import Response


class CountPaginationHeaders(LinkHeaderPagination):
    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        first_url = self.get_first_link()
        last_url = self.get_last_link()

        links = []
        for url, label in (
                (first_url, 'first'),
                (previous_url, 'prev'),
                (next_url, 'next'),
                (last_url, 'last'),
        ):
            if url is not None:
                links.append('<{}>; rel="{}"'.format(url, label))
        headers = {'Link': ', '.join(links)} if links else {}
        headers['Next-Page'] = self.page.next_page_number() if self.page.has_next() else None
        headers['Previous-Page'] = self.page.previous_page_number() if self.page.has_previous() else None
        headers['Last-Page'] = self.page.paginator.num_pages
        headers['Count'] = self.page.paginator.count
        return Response(data, headers=headers)
