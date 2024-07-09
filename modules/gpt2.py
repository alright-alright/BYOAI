<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta property="og:title" content="openai-community/gpt2 · Hugging Face" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/openai-community/gpt2" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/models/openai-community/gpt2.png" />

		<link rel="stylesheet" href="/front/build/kube-0e905ea/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		<link rel="canonical" href="https://huggingface.co/openai-community/gpt2">  

		<title>openai-community/gpt2 · Hugging Face</title>

		<script
			defer
			data-domain="huggingface.co"
			event-loggedIn="false"
			src="/js/script.pageview-props.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
		<script>
			window.hubConfig = JSON.parse(`{"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https://huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","captchaDisabledOnSignup":true,"datasetViewerPublicUrl":"https://datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https://api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDevApiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w","logoDevApiUrl":"https://img.logo.dev/"}`);
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script>
	</head>
	<body class="flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black ModelPage">
		<div class="flex min-h-screen flex-col">
	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;classNames&quot;:&quot;&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-1.5 xl:space-x-2"><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/posts"><svg class="mr-1.5 text-gray-400 group-hover:text-yellow-500 !text-yellow-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet"><path fill="currentColor" fill-rule="evenodd" d="M3.73 2.4A4.25 4.25 0 1 1 6 10.26H2.17l-.13-.02a.43.43 0 0 1-.3-.43l.01-.06a.43.43 0 0 1 .12-.22l.84-.84A4.26 4.26 0 0 1 3.73 2.4Z" clip-rule="evenodd"></path></svg>
					Posts</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li class="max-2xl:hidden"><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
		</button>
	
	
	</div></li>
		<li><a class="group flex items-center px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><a class="block cursor-pointer px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/login">Log In
				</a></li>
			<li><a class="rounded-full border border-transparent bg-gray-900 px-3 py-1 leading-none text-white hover:border-black hover:bg-white hover:text-black" href="/join">Sign Up
					</a></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{}"></div>
	

	<main class="flex flex-1 flex-col"><div class="SVELTE_HYDRATER contents" data-target="ModelHeader" data-props="{&quot;activeTab&quot;:&quot;modelCard&quot;,&quot;author&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/9NY4jfufqo1uyv8oNXQju.png&quot;,&quot;fullname&quot;:&quot;OpenAI community&quot;,&quot;name&quot;:&quot;openai-community&quot;,&quot;type&quot;:&quot;org&quot;,&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;isEnterprise&quot;:false},&quot;canReadRepoSettings&quot;:false,&quot;canWriteRepoContent&quot;:false,&quot;canDisable&quot;:false,&quot;hasGatedAccess&quot;:true,&quot;model&quot;:{&quot;author&quot;:&quot;openai-community&quot;,&quot;cardData&quot;:{&quot;language&quot;:&quot;en&quot;,&quot;tags&quot;:[&quot;exbert&quot;],&quot;license&quot;:&quot;mit&quot;},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;architectures&quot;:[&quot;GPT2LMHeadModel&quot;],&quot;model_type&quot;:&quot;gpt2&quot;,&quot;tokenizer_config&quot;:{}},&quot;createdAt&quot;:&quot;2022-03-02T23:29:04.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;downloads&quot;:6888015,&quot;downloadsAllTime&quot;:592183811,&quot;doi&quot;:{&quot;id&quot;:&quot;10.57967/hf/0039&quot;,&quot;commit&quot;:&quot;909a290700bd99135e67c64eefc166960b67cfd2&quot;},&quot;id&quot;:&quot;openai-community/gpt2&quot;,&quot;isLikedByUser&quot;:false,&quot;isWatchedByUser&quot;:false,&quot;inference&quot;:&quot;Yes&quot;,&quot;lastModified&quot;:&quot;2024-02-19T10:57:45.000Z&quot;,&quot;likes&quot;:2076,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;pwcLink&quot;:{&quot;error&quot;:&quot;Unknown error, can't generate link to Papers With Code.&quot;},&quot;tags&quot;:[&quot;transformers&quot;,&quot;pytorch&quot;,&quot;tf&quot;,&quot;jax&quot;,&quot;tflite&quot;,&quot;rust&quot;,&quot;onnx&quot;,&quot;safetensors&quot;,&quot;gpt2&quot;,&quot;text-generation&quot;,&quot;exbert&quot;,&quot;en&quot;,&quot;doi:10.57967/hf/0039&quot;,&quot;license:mit&quot;,&quot;autotrain_compatible&quot;,&quot;text-generation-inference&quot;,&quot;endpoints_compatible&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;text-generation&quot;,&quot;label&quot;:&quot;Text Generation&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;nlp&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;pytorch&quot;,&quot;label&quot;:&quot;PyTorch&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tf&quot;,&quot;label&quot;:&quot;TensorFlow&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;jax&quot;,&quot;label&quot;:&quot;JAX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tflite&quot;,&quot;label&quot;:&quot;TF Lite&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;rust&quot;,&quot;label&quot;:&quot;Rust&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;onnx&quot;,&quot;label&quot;:&quot;ONNX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;safetensors&quot;,&quot;label&quot;:&quot;Safetensors&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;en&quot;,&quot;label&quot;:&quot;English&quot;,&quot;type&quot;:&quot;language&quot;},{&quot;id&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;label&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;type&quot;:&quot;doi&quot;},{&quot;id&quot;:&quot;gpt2&quot;,&quot;label&quot;:&quot;gpt2&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;exbert&quot;,&quot;label&quot;:&quot;exbert&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;autotrain_compatible&quot;,&quot;label&quot;:&quot;AutoTrain Compatible&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;text-generation-inference&quot;,&quot;label&quot;:&quot;text-generation-inference&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;endpoints_compatible&quot;,&quot;label&quot;:&quot;Inference Endpoints&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;license:mit&quot;,&quot;label&quot;:&quot;mit&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModelForCausalLM&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;processor&quot;:&quot;AutoTokenizer&quot;},&quot;widgetData&quot;:[{&quot;text&quot;:&quot;My name is Julien and I like to&quot;},{&quot;text&quot;:&quot;My name is Thomas and my main&quot;},{&quot;text&quot;:&quot;My name is Mariama, my favorite&quot;},{&quot;text&quot;:&quot;My name is Clara and I am&quot;},{&quot;text&quot;:&quot;My name is Lewis and I like to&quot;},{&quot;text&quot;:&quot;My name is Merve and my favorite&quot;},{&quot;text&quot;:&quot;My name is Teven and I am&quot;},{&quot;text&quot;:&quot;Once upon a time,&quot;}],&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;F32&quot;:137022720},&quot;total&quot;:137022720,&quot;sharded&quot;:false},&quot;inferenceLoadInfo&quot;:{&quot;compute_type&quot;:&quot;cpu&quot;,&quot;state&quot;:&quot;Loadable&quot;},&quot;inferenceStatus&quot;:&quot;loaded&quot;},&quot;discussionsStats&quot;:{&quot;closed&quot;:49,&quot;open&quot;:44,&quot;total&quot;:93},&quot;query&quot;:{}}"><header class="from-gray-50-to-white border-b border-gray-100 bg-gradient-to-t via-white dark:via-gray-950 pt-6 sm:pt-9"><div class="container relative "><h1 class="flex flex-wrap items-center leading-tight mb-3 text-lg max-sm:gap-y-1.5 md:text-xl">
			<div class="group flex flex-none items-center"><div class="relative mr-1.5 flex items-center">

			<img alt="" class="w-3.5 h-3.5 rounded  flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/5dd96eb166059660ed1ee413/9NY4jfufqo1uyv8oNXQju.png" crossorigin="anonymous"></div>
		<a href="/openai-community" class="text-gray-400 hover:text-blue-600">openai-community</a>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full "><a class="break-words font-mono font-semibold hover:text-blue-600 " href="/openai-community/gpt2">gpt2</a>
	<button class="relative text-sm mr-4 inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy model name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">2.08k</button></div>




			
	</h1>
		<div class="mb-3 flex flex-wrap md:mb-4"><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?pipeline_tag=text-generation"><div class="tag tag-white  "><div class="tag-ico -ml-2 tag-ico-indigo"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 18 18"><path d="M16.2607 8.08202L14.468 6.28928C14.3063 6.12804 14.0873 6.03749 13.859 6.03749C13.6307 6.03749 13.4117 6.12804 13.25 6.28928L5.6375 13.904V16.9125H8.64607L16.2607 9.30002C16.422 9.13836 16.5125 8.91935 16.5125 8.69102C16.5125 8.4627 16.422 8.24369 16.2607 8.08202V8.08202ZM8.1953 15.825H6.725V14.3547L11.858 9.22118L13.3288 10.6915L8.1953 15.825ZM14.0982 9.92262L12.6279 8.45232L13.8606 7.21964L15.3309 8.68994L14.0982 9.92262Z"></path><path d="M6.18125 9.84373H7.26875V6.03748H8.9V4.94998H4.55V6.03748H6.18125V9.84373Z"></path><path d="M4.55 11.475H2.375V2.775H11.075V4.95H12.1625V2.775C12.1625 2.48658 12.0479 2.20997 11.844 2.00602C11.64 1.80208 11.3634 1.6875 11.075 1.6875H2.375C2.08658 1.6875 1.80997 1.80208 1.60602 2.00602C1.40207 2.20997 1.2875 2.48658 1.2875 2.775V11.475C1.2875 11.7634 1.40207 12.04 1.60602 12.244C1.80997 12.4479 2.08658 12.5625 2.375 12.5625H4.55V11.475Z"></path></svg></div>

	

	<span>Text Generation</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=transformers"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 95 88"><path fill="#fff" d="M94.25 70.08a8.28 8.28 0 0 1-.43 6.46 10.57 10.57 0 0 1-3 3.6 25.18 25.18 0 0 1-5.7 3.2 65.74 65.74 0 0 1-7.56 2.65 46.67 46.67 0 0 1-11.42 1.68c-5.42.05-10.09-1.23-13.4-4.5a40.4 40.4 0 0 1-10.14.03c-3.34 3.25-7.99 4.52-13.39 4.47a46.82 46.82 0 0 1-11.43-1.68 66.37 66.37 0 0 1-7.55-2.65c-2.28-.98-4.17-2-5.68-3.2a10.5 10.5 0 0 1-3.02-3.6c-.99-2-1.18-4.3-.42-6.46a8.54 8.54 0 0 1-.33-5.63c.25-.95.66-1.83 1.18-2.61a8.67 8.67 0 0 1 2.1-8.47 8.23 8.23 0 0 1 2.82-2.07 41.75 41.75 0 1 1 81.3-.12 8.27 8.27 0 0 1 3.11 2.19 8.7 8.7 0 0 1 2.1 8.47c.52.78.93 1.66 1.18 2.61a8.61 8.61 0 0 1-.32 5.63Z"></path><path fill="#FFD21E" d="M47.21 76.5a34.75 34.75 0 1 0 0-69.5 34.75 34.75 0 0 0 0 69.5Z"></path><path fill="#FF9D0B" d="M81.96 41.75a34.75 34.75 0 1 0-69.5 0 34.75 34.75 0 0 0 69.5 0Zm-73.5 0a38.75 38.75 0 1 1 77.5 0 38.75 38.75 0 0 1-77.5 0Z"></path><path fill="#3A3B45" d="M58.5 32.3c1.28.44 1.78 3.06 3.07 2.38a5 5 0 1 0-6.76-2.07c.61 1.15 2.55-.72 3.7-.32ZM34.95 32.3c-1.28.44-1.79 3.06-3.07 2.38a5 5 0 1 1 6.76-2.07c-.61 1.15-2.56-.72-3.7-.32Z"></path><path fill="#FF323D" d="M46.96 56.29c9.83 0 13-8.76 13-13.26 0-2.34-1.57-1.6-4.09-.36-2.33 1.15-5.46 2.74-8.9 2.74-7.19 0-13-6.88-13-2.38s3.16 13.26 13 13.26Z"></path><path fill="#3A3B45" fill-rule="evenodd" d="M39.43 54a8.7 8.7 0 0 1 5.3-4.49c.4-.12.81.57 1.24 1.28.4.68.82 1.37 1.24 1.37.45 0 .9-.68 1.33-1.35.45-.7.89-1.38 1.32-1.25a8.61 8.61 0 0 1 5 4.17c3.73-2.94 5.1-7.74 5.1-10.7 0-2.34-1.57-1.6-4.09-.36l-.14.07c-2.31 1.15-5.39 2.67-8.77 2.67s-6.45-1.52-8.77-2.67c-2.6-1.29-4.23-2.1-4.23.29 0 3.05 1.46 8.06 5.47 10.97Z" clip-rule="evenodd"></path><path fill="#FF9D0B" d="M70.71 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM24.21 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM17.52 48c-1.62 0-3.06.66-4.07 1.87a5.97 5.97 0 0 0-1.33 3.76 7.1 7.1 0 0 0-1.94-.3c-1.55 0-2.95.59-3.94 1.66a5.8 5.8 0 0 0-.8 7 5.3 5.3 0 0 0-1.79 2.82c-.24.9-.48 2.8.8 4.74a5.22 5.22 0 0 0-.37 5.02c1.02 2.32 3.57 4.14 8.52 6.1 3.07 1.22 5.89 2 5.91 2.01a44.33 44.33 0 0 0 10.93 1.6c5.86 0 10.05-1.8 12.46-5.34 3.88-5.69 3.33-10.9-1.7-15.92-2.77-2.78-4.62-6.87-5-7.77-.78-2.66-2.84-5.62-6.25-5.62a5.7 5.7 0 0 0-4.6 2.46c-1-1.26-1.98-2.25-2.86-2.82A7.4 7.4 0 0 0 17.52 48Zm0 4c.51 0 1.14.22 1.82.65 2.14 1.36 6.25 8.43 7.76 11.18.5.92 1.37 1.31 2.14 1.31 1.55 0 2.75-1.53.15-3.48-3.92-2.93-2.55-7.72-.68-8.01.08-.02.17-.02.24-.02 1.7 0 2.45 2.93 2.45 2.93s2.2 5.52 5.98 9.3c3.77 3.77 3.97 6.8 1.22 10.83-1.88 2.75-5.47 3.58-9.16 3.58-3.81 0-7.73-.9-9.92-1.46-.11-.03-13.45-3.8-11.76-7 .28-.54.75-.76 1.34-.76 2.38 0 6.7 3.54 8.57 3.54.41 0 .7-.17.83-.6.79-2.85-12.06-4.05-10.98-8.17.2-.73.71-1.02 1.44-1.02 3.14 0 10.2 5.53 11.68 5.53.11 0 .2-.03.24-.1.74-1.2.33-2.04-4.9-5.2-5.21-3.16-8.88-5.06-6.8-7.33.24-.26.58-.38 1-.38 3.17 0 10.66 6.82 10.66 6.82s2.02 2.1 3.25 2.1c.28 0 .52-.1.68-.38.86-1.46-8.06-8.22-8.56-11.01-.34-1.9.24-2.85 1.31-2.85Z"></path><path fill="#FFD21E" d="M38.6 76.69c2.75-4.04 2.55-7.07-1.22-10.84-3.78-3.77-5.98-9.3-5.98-9.3s-.82-3.2-2.69-2.9c-1.87.3-3.24 5.08.68 8.01 3.91 2.93-.78 4.92-2.29 2.17-1.5-2.75-5.62-9.82-7.76-11.18-2.13-1.35-3.63-.6-3.13 2.2.5 2.79 9.43 9.55 8.56 11-.87 1.47-3.93-1.71-3.93-1.71s-9.57-8.71-11.66-6.44c-2.08 2.27 1.59 4.17 6.8 7.33 5.23 3.16 5.64 4 4.9 5.2-.75 1.2-12.28-8.53-13.36-4.4-1.08 4.11 11.77 5.3 10.98 8.15-.8 2.85-9.06-5.38-10.74-2.18-1.7 3.21 11.65 6.98 11.76 7.01 4.3 1.12 15.25 3.49 19.08-2.12Z"></path><path fill="#FF9D0B" d="M77.4 48c1.62 0 3.07.66 4.07 1.87a5.97 5.97 0 0 1 1.33 3.76 7.1 7.1 0 0 1 1.95-.3c1.55 0 2.95.59 3.94 1.66a5.8 5.8 0 0 1 .8 7 5.3 5.3 0 0 1 1.78 2.82c.24.9.48 2.8-.8 4.74a5.22 5.22 0 0 1 .37 5.02c-1.02 2.32-3.57 4.14-8.51 6.1-3.08 1.22-5.9 2-5.92 2.01a44.33 44.33 0 0 1-10.93 1.6c-5.86 0-10.05-1.8-12.46-5.34-3.88-5.69-3.33-10.9 1.7-15.92 2.78-2.78 4.63-6.87 5.01-7.77.78-2.66 2.83-5.62 6.24-5.62a5.7 5.7 0 0 1 4.6 2.46c1-1.26 1.98-2.25 2.87-2.82A7.4 7.4 0 0 1 77.4 48Zm0 4c-.51 0-1.13.22-1.82.65-2.13 1.36-6.25 8.43-7.76 11.18a2.43 2.43 0 0 1-2.14 1.31c-1.54 0-2.75-1.53-.14-3.48 3.91-2.93 2.54-7.72.67-8.01a1.54 1.54 0 0 0-.24-.02c-1.7 0-2.45 2.93-2.45 2.93s-2.2 5.52-5.97 9.3c-3.78 3.77-3.98 6.8-1.22 10.83 1.87 2.75 5.47 3.58 9.15 3.58 3.82 0 7.73-.9 9.93-1.46.1-.03 13.45-3.8 11.76-7-.29-.54-.75-.76-1.34-.76-2.38 0-6.71 3.54-8.57 3.54-.42 0-.71-.17-.83-.6-.8-2.85 12.05-4.05 10.97-8.17-.19-.73-.7-1.02-1.44-1.02-3.14 0-10.2 5.53-11.68 5.53-.1 0-.19-.03-.23-.1-.74-1.2-.34-2.04 4.88-5.2 5.23-3.16 8.9-5.06 6.8-7.33-.23-.26-.57-.38-.98-.38-3.18 0-10.67 6.82-10.67 6.82s-2.02 2.1-3.24 2.1a.74.74 0 0 1-.68-.38c-.87-1.46 8.05-8.22 8.55-11.01.34-1.9-.24-2.85-1.31-2.85Z"></path><path fill="#FFD21E" d="M56.33 76.69c-2.75-4.04-2.56-7.07 1.22-10.84 3.77-3.77 5.97-9.3 5.97-9.3s.82-3.2 2.7-2.9c1.86.3 3.23 5.08-.68 8.01-3.92 2.93.78 4.92 2.28 2.17 1.51-2.75 5.63-9.82 7.76-11.18 2.13-1.35 3.64-.6 3.13 2.2-.5 2.79-9.42 9.55-8.55 11 .86 1.47 3.92-1.71 3.92-1.71s9.58-8.71 11.66-6.44c2.08 2.27-1.58 4.17-6.8 7.33-5.23 3.16-5.63 4-4.9 5.2.75 1.2 12.28-8.53 13.36-4.4 1.08 4.11-11.76 5.3-10.97 8.15.8 2.85 9.05-5.38 10.74-2.18 1.69 3.21-11.65 6.98-11.76 7.01-4.31 1.12-15.26 3.49-19.08-2.12Z"></path></svg>

	

	<span>Transformers</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=pytorch"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><defs><clipPath id="icon-pytorch-a"><rect x="3.05" y="0.5" width="25.73" height="31" fill="none"></rect></clipPath></defs><g clip-path="url(#icon-pytorch-a)"><path d="M24.94,9.51a12.81,12.81,0,0,1,0,18.16,12.68,12.68,0,0,1-18,0,12.81,12.81,0,0,1,0-18.16l9-9V5l-.84.83-6,6a9.58,9.58,0,1,0,13.55,0ZM20.44,9a1.68,1.68,0,1,1,1.67-1.67A1.68,1.68,0,0,1,20.44,9Z" fill="#ee4c2c"></path></g></svg>

	

	<span>PyTorch</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=tf"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 534.01 508.99"><defs><style>.cls-1 {
				fill: none;
			}
			.cls-2 {
				clip-path: url(#clip-path);
			}
			.cls-3 {
				fill: url(#linear-gradient);
			}
			.cls-4 {
				clip-path: url(#clip-path-2);
			}
			.cls-5 {
				fill: url(#linear-gradient-2);
			}
		</style><clipPath id="clip-path" transform="translate(23.09 1.92)"><polygon class="cls-1" points="452.23 123.16 235.73 0 235.73 506.11 322.33 456.07 322.33 313.67 387.76 351.2 386.8 254.02 322.33 216.49 322.33 159.72 452.23 235.73 452.23 123.16"></polygon></clipPath><linearGradient id="linear-gradient" x1="-20.21" y1="-48.36" x2="510.92" y2="-48.36" gradientTransform="matrix(1, 0, 0, -1, 0, 204.21)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ff6f00"></stop><stop offset="1" stop-color="#ffa800"></stop></linearGradient><clipPath id="clip-path-2" transform="translate(23.09 1.92)"><polygon class="cls-1" points="0 123.16 216.49 0 216.49 506.11 129.89 456.07 129.89 159.72 0 235.73 0 123.16"></polygon></clipPath><linearGradient id="linear-gradient-2" x1="-23.09" y1="-48.36" x2="508.03" y2="-48.36" xlink:href="#linear-gradient"></linearGradient></defs><title>google-tensorflow</title><g class="cls-2"><path class="cls-3" d="M-20.21-1.92H510.92v509H-20.21Z" transform="translate(23.09 1.92)"></path></g><g class="cls-4"><path class="cls-5" d="M-23.09-1.92H508v509H-23.09Z" transform="translate(23.09 1.92)"></path></g></svg>

	

	<span>TensorFlow</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=jax"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1.73em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 451 260.81"><style>.J {
			stroke: #dce0df;
		}
		.K {
			stroke-linejoin: round;
		}
	</style><g fill="#5e97f6" class="J K"><path d="M50.5 130.4l-25 43.31h50l25-43.31h-50z"></path><path d="M.5 217.01l25-43.3h50l-25 43.3H.5z"></path><path d="M125.5 173.71h-50l-25 43.3h50l25-43.3z"></path><path d="M175.5 173.71h-50l-25 43.3h50l25-43.3z"></path><path d="M150.5 130.4l-25 43.31h50l25-43.31h-50z"></path><path d="M175.5 87.1l-25 43.3h50l25-43.3h-50z"></path><path d="M200.5 43.8l-25 43.3h50l25-43.3h-50z"></path><path d="M225.5.5l-25 43.3h50l25-43.3h-50z"></path></g><g fill="#2a56c6" class="J K"><path d="M.5 217.01l25 43.3h50l-25-43.3H.5z"></path><path d="M125.5 260.31h-50l-25-43.3h50l25 43.3z"></path><path d="M175.5 260.31h-50l-25-43.3h50l25 43.3z"></path></g><g fill="#00796b" class="J K"><path d="M200.5 217.01l-25-43.3-25 43.3 25 43.3 25-43.3zm50-86.61l-25-43.3-25 43.3h50z"></path><path d="M250.5 43.8l-25 43.3 25 43.3 25-43.3-25-43.3z"></path></g><path d="M125.5 173.71l-25-43.31-25 43.31h50z" fill="#3367d6" class="J K"></path><g fill="#26a69a" class="J K"><path d="M250.5 130.4h-50l-25 43.31h50l25-43.31z"></path><path d="M300.5 130.4h-50l-25 43.31h50l25-43.31z"></path></g><g fill="#9c27b0" class="J K"><path d="M350.5 43.8L325.5.5l-25 43.3 25 43.3 25-43.3z"></path><path d="M375.5 87.1l-25-43.3-25 43.3 25 43.3 25-43.3z"></path><path d="M400.5 130.4l-25-43.3-25 43.3 25 43.31 25-43.31z"></path><path d="M425.5 173.71l-25-43.31-25 43.31 25 43.3 25-43.3z"></path><path d="M450.5 217.01l-25-43.3-25 43.3 25 43.3 25-43.3zM425.5.5l-25 43.3 25 43.3 25-43.3-25-43.3z"></path><path d="M375.5 87.1l25-43.3 25 43.3-25 43.3-25-43.3zm-25 43.3l-25 43.31 25 43.3 25-43.3-25-43.31z"></path><path d="M325.5 260.31l-25-43.3 25-43.3 25 43.3-25 43.3z"></path></g><path d="M275.5 260.31l-25-43.3h50l25 43.3h-50z" fill="#6a1b9a" class="J K"></path><g fill="#00695c" class="J K"><path d="M225.5 173.71h-50l25 43.3h50l-25-43.3z"></path><path d="M275.5 173.71h-50l25 43.3 25-43.3zm0-86.61l25 43.3h50l-25-43.3h-50z"></path><path d="M300.5 43.8h-50l25 43.3h50l-25-43.3zm125 216.51l-25-43.3h-50l25 43.3h50z"></path><path d="M375.5 173.71l-25 43.3h50l-25-43.3z"></path></g><g fill="#ea80fc" class="J K"><path d="M325.5.5h-50l-25 43.3h50l25-43.3zm0 173.21h-50l-25 43.3h50l25-43.3z"></path><path d="M350.5 130.4h-50l-25 43.31h50l25-43.31zM425.5.5h-50l-25 43.3h50l25-43.3z"></path><path d="M375.5 87.1l-25-43.3h50l-25 43.3z"></path></g></svg>

	

	<span>JAX</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=tflite"><div class="tag tag-white  ">

	

	<span>TF Lite</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=rust"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 32 32"><path d="M31.77,15.61l-1.34-.83c0-.13,0-.26,0-.39l1.16-1.08a.46.46,0,0,0,.14-.43.44.44,0,0,0-.29-.34L29.92,12l-.12-.38.92-1.28a.46.46,0,0,0,.06-.45.47.47,0,0,0-.36-.28l-1.55-.25L28.68,9l.66-1.44a.48.48,0,0,0,0-.45.46.46,0,0,0-.4-.2L27.32,7l-.25-.3.36-1.54a.46.46,0,0,0-.12-.43.46.46,0,0,0-.43-.13l-1.54.37L25,4.68l.06-1.58a.44.44,0,0,0-.21-.4.45.45,0,0,0-.45,0L23,3.32l-.35-.19L22.4,1.57a.46.46,0,0,0-.28-.35.48.48,0,0,0-.45.05l-1.28.92L20,2.08,19.46.6a.44.44,0,0,0-.34-.29.46.46,0,0,0-.43.14L17.62,1.6l-.39,0L16.39.22a.46.46,0,0,0-.78,0l-.83,1.34-.39,0L13.31.45a.46.46,0,0,0-.43-.14.44.44,0,0,0-.34.29L12,2.08l-.38.11-1.28-.92a.48.48,0,0,0-.45-.05.5.5,0,0,0-.28.35L9.35,3.13,9,3.32,7.57,2.66a.45.45,0,0,0-.45,0,.49.49,0,0,0-.21.4L7,4.68l-.31.25L5.13,4.56a.48.48,0,0,0-.44.13.46.46,0,0,0-.12.43l.36,1.54L4.68,7l-1.58,0a.46.46,0,0,0-.4.2.48.48,0,0,0,0,.45L3.32,9l-.19.35L1.57,9.6a.47.47,0,0,0-.35.28.48.48,0,0,0,.05.45l.92,1.28c0,.12-.07.25-.11.38L.6,12.54a.44.44,0,0,0-.29.34.46.46,0,0,0,.14.43L1.6,14.39l0,.39-1.35.83a.47.47,0,0,0,0,.78l1.35.84,0,.39L.45,18.69a.46.46,0,0,0-.14.43.44.44,0,0,0,.29.34L2.08,20c0,.13.07.26.11.39l-.92,1.28a.46.46,0,0,0-.05.44.45.45,0,0,0,.36.28l1.55.25.19.35-.65,1.44a.45.45,0,0,0,.43.65L4.68,25l.25.3-.36,1.54a.46.46,0,0,0,.12.43.48.48,0,0,0,.44.12l1.54-.36.3.25L6.91,28.9a.49.49,0,0,0,.21.4.48.48,0,0,0,.45,0L9,28.68l.35.19.26,1.56a.46.46,0,0,0,.27.35.48.48,0,0,0,.45-.05l1.28-.92.38.12.55,1.47a.47.47,0,0,0,.34.29.46.46,0,0,0,.43-.13l1.08-1.16.39,0,.83,1.34A.46.46,0,0,0,16,32a.47.47,0,0,0,.4-.22l.83-1.34.39,0,1.08,1.16a.46.46,0,0,0,.43.13.47.47,0,0,0,.34-.29L20,29.93l.38-.12,1.28.92a.48.48,0,0,0,.45.05.45.45,0,0,0,.27-.35l.26-1.56.35-.19,1.43.66a.48.48,0,0,0,.45,0,.49.49,0,0,0,.21-.4L25,27.32l.3-.25,1.54.36a.48.48,0,0,0,.44-.12.46.46,0,0,0,.12-.43l-.36-1.54.25-.3,1.58.05a.45.45,0,0,0,.43-.65L28.69,23l.19-.35,1.55-.25a.45.45,0,0,0,.36-.28.43.43,0,0,0-.06-.44l-.92-1.28.12-.39,1.48-.55a.44.44,0,0,0,.29-.34.46.46,0,0,0-.14-.43L30.4,17.62c0-.13,0-.26,0-.39l1.34-.84a.46.46,0,0,0,0-.78Zm-9,11.16A1,1,0,1,1,23.92,26a.95.95,0,0,1-1.14.73Zm-.45-3.09a.87.87,0,0,0-1,.67l-.48,2.22a11.74,11.74,0,0,1-9.75,0l-.48-2.23a.85.85,0,0,0-1-.66l-2,.42a14.67,14.67,0,0,1-1-1.2h9.58c.1,0,.18,0,.18-.12V19.35c0-.1-.08-.12-.18-.12h-2.8V17.08h3a1.9,1.9,0,0,1,1.86,1.62c.12.47.39,2,.57,2.5s.91,1.65,1.69,1.65h4.77l.17,0a11,11,0,0,1-1.08,1.27l-2-.43Zm-13.24,3A.94.94,0,0,1,8,26a1,1,0,1,1,1.13.73ZM5.45,12a1,1,0,0,1-1.74.77,1,1,0,0,1,.49-1.26A1,1,0,0,1,5.45,12ZM4.33,14.66l2.05-.91a.87.87,0,0,0,.44-1.15l-.42-.95H8.06v7.46H4.73a11.37,11.37,0,0,1-.45-3.21,10.41,10.41,0,0,1,.07-1.26Zm9-.73v-2.2h3.95c.2,0,1.44.24,1.44,1.16,0,.77-.95,1-1.73,1H13.32Zm14.34,2q0,.45,0,.87h-1.2c-.12,0-.17.08-.17.2v.55c0,1.3-.73,1.58-1.37,1.65s-1.29-.25-1.37-.63a4.13,4.13,0,0,0-1.91-3.21C22.79,14.59,24,13.49,24,12a3.76,3.76,0,0,0-1.83-3.09,5.22,5.22,0,0,0-2.52-.83H7.25a11.79,11.79,0,0,1,6.54-3.7l1.47,1.54a.87.87,0,0,0,1.22,0l1.64-1.57a11.69,11.69,0,0,1,8,5.72L25,12.64a.87.87,0,0,0,.44,1.14l2.16,1a11.46,11.46,0,0,1,.06,1.17ZM15.25,3.1a1,1,0,0,1,1.34,0,1,1,0,0,1,0,1.35,1,1,0,0,1-1.34,0,1,1,0,0,1,0-1.35Zm11.13,9a.94.94,0,0,1,1.25-.48,1,1,0,1,1-1.25.48Z" fill="currentColor"></path></svg>

	

	<span>Rust</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=onnx"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30.7,15h-.2L25.16,5.09a1.26,1.26,0,0,0,.15-.59A1.3,1.3,0,0,0,24,3.2a1.27,1.27,0,0,0-.93.4L12.43,1.48A1.29,1.29,0,1,0,10,2.24L1.7,14.13a1.21,1.21,0,0,0-.34-.05,1.3,1.3,0,0,0,0,2.59h0l4.5,11.07a1.38,1.38,0,0,0-.12.54,1.3,1.3,0,0,0,1.3,1.29,1.27,1.27,0,0,0,.94-.4l13.44,1.31A1.29,1.29,0,0,0,24,30.16a1.34,1.34,0,0,0-.31-.84l6.77-11.8h.22A1.3,1.3,0,0,0,32,16.24,1.28,1.28,0,0,0,30.7,15ZM23,5.29a1.26,1.26,0,0,0,.61.44l-2,15.37a1.29,1.29,0,0,0-.36.14L10,11.52a.93.93,0,0,0,.05-.34c0-.08,0-.17,0-.25Zm6.47,11.32-6.89,4.71a1.28,1.28,0,0,0-.17-.1L24.45,5.69h0l5.26,9.7a1.27,1.27,0,0,0-.32.86ZM8.57,9.9a1.28,1.28,0,0,0-1.09,1.28v.09L2.86,14,10,3.74ZM9,12.45a1.54,1.54,0,0,0,.47-.21l11.11,9.67a1.45,1.45,0,0,0-.08.47v.07l-12.4,5.1A1.3,1.3,0,0,0,7.34,27ZM20.87,23.24a1.22,1.22,0,0,0,.65.39L22.13,29a1.34,1.34,0,0,0-.59.61l-13-1.28Zm1.53.29a1.33,1.33,0,0,0,.72-1.16.83.83,0,0,0-.05-.32l6.3-4.33L23,28.8Zm.32-19.08L9.58,10.17l-.15-.1L11.1,2.91h.05a1.26,1.26,0,0,0,1.08-.59L22.72,4.41ZM2.66,15.38c0-.09,0-.17,0-.24l5.19-3.06a1.41,1.41,0,0,0,.36.27L6.5,26.86,2.22,16.34A1.28,1.28,0,0,0,2.66,15.38Z" fill="#333"></path><path d="M24.49,5.69l5.25,9.7a1.32,1.32,0,0,0-.32.86,1.49,1.49,0,0,0,0,.36l-6.88,4.71-.17-.1,2-15.53Z" fill="#dededd"></path><path d="M22.4,23.53a1.33,1.33,0,0,0,.72-1.16.83.83,0,0,0-.05-.32l6.3-4.33L23,28.8Z" fill="#b2b2b2"></path><path d="M20.87,23.24a1.22,1.22,0,0,0,.65.39L22.13,29a1.34,1.34,0,0,0-.59.61l-13-1.28Z" fill="#d1d1d1"></path><path d="M9,12.45a1.54,1.54,0,0,0,.47-.21l11.11,9.67a1.45,1.45,0,0,0-.08.47v.07l-12.4,5.1A1.3,1.3,0,0,0,7.34,27Z" fill="#f2f2f2"></path><path d="M2.66,15.38c0-.09,0-.17,0-.24l5.19-3.06a1.41,1.41,0,0,0,.36.27L6.5,26.86,2.22,16.34A1.28,1.28,0,0,0,2.66,15.38Z" fill="#d8d8d7"></path><path d="M8.57,9.9a1.28,1.28,0,0,0-1.09,1.28v.09L2.86,14,10,3.74Z" fill="#b2b2b2"></path><path d="M22.72,4.45,9.58,10.17l-.15-.1L11.1,2.91h.05a1.26,1.26,0,0,0,1.08-.59L22.72,4.41Z" fill="#d1d1d1"></path><path d="M23,5.29a1.26,1.26,0,0,0,.61.44l-2,15.37a1.29,1.29,0,0,0-.36.14L10,11.52a.93.93,0,0,0,.05-.34c0-.08,0-.17,0-.25Z" fill="#fff"></path></svg>

	

	<span>ONNX</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?library=safetensors"><div class="tag tag-white  "><svg class="text-black inline-block text-sm" viewBox="0 0 57 44" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet"><path d="M36.816 20.1474L54.9918 27.4409C55.5142 27.6506 55.9623 28.0112 56.2788 28.4766C56.5954 28.9421 56.7661 29.4913 56.7691 30.0542C56.7722 30.6171 56.6074 31.1682 56.2959 31.637C55.9844 32.1059 55.5402 32.4713 55.0201 32.6866L29.953 43.0646C29.2593 43.3518 28.4799 43.3518 27.7862 43.0646L2.71624 32.6894C2.19613 32.4741 1.75197 32.1087 1.44044 31.6398C1.12892 31.171 0.964165 30.62 0.967204 30.057C0.970244 29.4941 1.14094 28.9449 1.45751 28.4794C1.77408 28.014 2.22216 27.6534 2.74456 27.4437L21.2404 20.0227C22.2997 19.5979 25.6477 20.8441 28.8682 20.8555C32.3096 20.8668 35.6292 19.6715 36.816 20.1474ZM11.3042 30.1119L28.8682 37.3828L46.435 30.1119L28.8682 23.0619L11.3042 30.1119ZM29.9247 0.388251L54.9918 10.4462C55.5142 10.6559 55.9623 11.0165 56.2788 11.482C56.5954 11.9474 56.7661 12.4967 56.7691 13.0596C56.7722 13.6225 56.6074 14.1735 56.2959 14.6424C55.9844 15.1112 55.5402 15.4766 55.0201 15.6919L29.953 26.07C29.2593 26.3572 28.4799 26.3572 27.7862 26.07L2.71624 15.6948C2.19613 15.4795 1.75197 15.1141 1.44044 14.6452C1.12892 14.1763 0.964165 13.6253 0.967204 13.0624C0.970244 12.4995 1.14094 11.9503 1.45751 11.4848C1.77408 11.0193 2.22216 10.6588 2.74456 10.4491L27.8117 0.388251C28.4896 0.1157 29.2467 0.1157 29.9247 0.388251ZM11.3042 13.1172L28.8682 20.3881L46.435 13.1172L28.8682 6.06729L11.3042 13.1172Z" fill="currentColor"></path></svg>

	

	<span>Safetensors</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?language=en"><div class="tag tag-white  ">
		<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="text-green-600/80" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 10 10"><path fill-rule="evenodd" clip-rule="evenodd" d="M0.625 5C0.625 6.16032 1.08594 7.27312 1.90641 8.09359C2.72688 8.91406 3.83968 9.375 5 9.375C6.16032 9.375 7.27312 8.91406 8.09359 8.09359C8.91406 7.27312 9.375 6.16032 9.375 5C9.375 3.83968 8.91406 2.72688 8.09359 1.90641C7.27312 1.08594 6.16032 0.625 5 0.625C3.83968 0.625 2.72688 1.08594 1.90641 1.90641C1.08594 2.72688 0.625 3.83968 0.625 5ZM7.64365 7.48027C7.61734 7.50832 7.59054 7.53598 7.56326 7.56326C7.13828 7.98824 6.61864 8.2968 6.0539 8.46842C6.29802 8.11949 6.49498 7.64804 6.63475 7.09483C7.00845 7.18834 7.35014 7.3187 7.64365 7.48027ZM8.10076 6.87776C8.37677 6.42196 8.55005 5.90894 8.60556 5.37499H6.86808C6.85542 5.71597 6.82551 6.04557 6.77971 6.35841C7.25309 6.47355 7.68808 6.6414 8.062 6.85549C8.07497 6.86283 8.08789 6.87025 8.10076 6.87776ZM6.03795 6.22536C6.07708 5.95737 6.1044 5.67232 6.11705 5.37499H3.88295C3.89666 5.69742 3.92764 6.00542 3.9722 6.29287C4.37075 6.21726 4.79213 6.17749 5.224 6.17749C5.50054 6.17749 5.77294 6.19376 6.03795 6.22536ZM4.1261 7.02673C4.34894 7.84835 4.68681 8.375 5 8.375C5.32122 8.375 5.66839 7.82101 5.8908 6.963C5.67389 6.93928 5.45082 6.92699 5.224 6.92699C4.84316 6.92699 4.47332 6.96176 4.1261 7.02673ZM3.39783 7.21853C3.53498 7.71842 3.72038 8.14579 3.9461 8.46842C3.42141 8.30898 2.93566 8.03132 2.52857 7.65192C2.77253 7.48017 3.06711 7.33382 3.39783 7.21853ZM3.23916 6.48077C3.18263 6.13193 3.14625 5.76074 3.13192 5.37499H1.39444C1.4585 5.99112 1.67936 6.57938 2.03393 7.08403C2.3706 6.83531 2.78055 6.63162 3.23916 6.48077ZM1.39444 4.62499H3.13192C3.14615 4.24204 3.18211 3.87344 3.23794 3.52681C2.77814 3.37545 2.36731 3.17096 2.03024 2.92123C1.67783 3.42469 1.45828 4.011 1.39444 4.62499ZM2.5237 2.35262C2.76812 2.52552 3.06373 2.67281 3.39584 2.78875C3.53318 2.28573 3.71928 1.85578 3.9461 1.53158C3.41932 1.69166 2.93178 1.97089 2.5237 2.35262ZM3.97101 3.71489C3.92709 4.00012 3.89654 4.30547 3.88295 4.62499H6.11705C6.10453 4.33057 6.07761 4.04818 6.03909 3.78248C5.77372 3.81417 5.50093 3.83049 5.224 3.83049C4.79169 3.83049 4.3699 3.79065 3.97101 3.71489ZM5.8928 3.04476C5.67527 3.06863 5.45151 3.08099 5.224 3.08099C4.84241 3.08099 4.47186 3.04609 4.12405 2.98086C4.34686 2.1549 4.68584 1.625 5 1.625C5.32218 1.625 5.67048 2.18233 5.8928 3.04476ZM6.78083 3.6493C6.826 3.95984 6.85552 4.28682 6.86808 4.62499H8.60556C8.55029 4.09337 8.37827 3.58251 8.10436 3.1282C8.0903 3.1364 8.07618 3.14449 8.062 3.15249C7.68838 3.36641 7.25378 3.53417 6.78083 3.6493ZM7.64858 2.52499C7.35446 2.68754 7.0117 2.81868 6.63664 2.91268C6.49676 2.35623 6.29913 1.88209 6.0539 1.53158C6.61864 1.7032 7.13828 2.01176 7.56326 2.43674C7.59224 2.46572 7.62068 2.49514 7.64858 2.52499Z" fill="currentColor"></path></svg>

	

	<span>English</span>
	

	</div></a>

	<div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-lg rounded-br-none " type="button">
		<div class="tag tag-white  relative rounded-br-none pr-2.5">

	

	<span>doi:10.57967/hf/0039</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 dark:border-b-gray-700 dark:border-r-gray-700"></div></div>
		
		</button>
	
	
	</div><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=gpt2"><div class="tag tag-white  ">

	

	<span>gpt2</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=exbert"><div class="tag tag-white  ">

	

	<span>exbert</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=text-generation-inference"><div class="tag tag-white  ">
		<svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill="#23B0FF" d="m9.6 3.6-3.2-2a1 1 0 0 0-1.1 0L2 3.7a1 1 0 0 0-.3 1.6H10a1 1 0 0 0-.3-1.6Z"></path><path fill="#2094FF" d="m6.7 9.7 3.2-4.5-.4-.8H5.7v4.8l1 .5Z"></path><path fill="#6BCAFF" d="M4.9 9.7 1.7 5.2l.4-.8h3.8v4.8l-1 .5Z"></path><path fill="#000" fill-rule="evenodd" d="M9.9 3.2c.8.5 1 1.5.5 2.3L7 10c-.6.9-2 .9-2.6 0L1.3 5.5c-.5-.8-.3-1.8.5-2.3l3.2-2c.5-.3 1.2-.3 1.7 0l3.2 2ZM6.4 5h3l-3 4.2V5ZM5.3 5h-3l3 4.2V5Zm3.8-1L6 2a.5.5 0 0 0-.5 0L2.6 4H9Z" clip-rule="evenodd"></path></svg>

	

	<span>text-generation-inference</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/models?other=endpoints_compatible"><div class="tag tag-white  ">
		<svg class="" width="1em" height="1em" viewBox="0 0 74 75" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M46.6517 14.9309C48.2799 11.0495 45.4292 6.76251 41.2202 6.76251H24.1817C19.8066 6.76251 15.9021 9.50789 14.4218 13.6249L8.51785 30.0453C6.77792 34.8844 6.77792 40.1785 8.51785 45.0177L14.4218 61.438C15.9021 65.5551 19.8066 68.3004 24.1817 68.3004H41.2202C45.4292 68.3004 48.2799 64.0134 46.6517 60.132L40.7616 46.0903C38.465 40.6155 38.465 34.4475 40.7616 28.9727L46.6517 14.9309Z" fill="#861FFF" stroke="black" stroke-width="12.6835" stroke-linejoin="round"></path><circle cx="53.1334" cy="37.5315" r="13.9518" fill="#FF3270" stroke="black" stroke-width="12.6835" stroke-linejoin="round"></circle></svg>

	

	
		<span>Inference Endpoints</span>
	

	</div></a><div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div class="tag tag-white rounded-full relative rounded-br-none pr-2.5">
		<svg class="text-xs text-gray-900" width="1em" height="1em" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.46009 5.0945V6.88125C1.46009 7.25201 1.75937 7.55129 2.13012 7.55129C2.50087 7.55129 2.80016 7.25201 2.80016 6.88125V5.0945C2.80016 4.72375 2.50087 4.42446 2.13012 4.42446C1.75937 4.42446 1.46009 4.72375 1.46009 5.0945ZM4.14022 5.0945V6.88125C4.14022 7.25201 4.4395 7.55129 4.81026 7.55129C5.18101 7.55129 5.48029 7.25201 5.48029 6.88125V5.0945C5.48029 4.72375 5.18101 4.42446 4.81026 4.42446C4.4395 4.42446 4.14022 4.72375 4.14022 5.0945ZM1.23674 9.78473H8.38377C8.75452 9.78473 9.0538 9.48545 9.0538 9.1147C9.0538 8.74395 8.75452 8.44466 8.38377 8.44466H1.23674C0.865993 8.44466 0.566711 8.74395 0.566711 9.1147C0.566711 9.48545 0.865993 9.78473 1.23674 9.78473ZM6.82036 5.0945V6.88125C6.82036 7.25201 7.11964 7.55129 7.49039 7.55129C7.86114 7.55129 8.16042 7.25201 8.16042 6.88125V5.0945C8.16042 4.72375 7.86114 4.42446 7.49039 4.42446C7.11964 4.42446 6.82036 4.72375 6.82036 5.0945ZM4.39484 0.623142L0.865993 2.48137C0.682851 2.57517 0.566711 2.76725 0.566711 2.97273C0.566711 3.28094 0.816857 3.53109 1.12507 3.53109H8.49991C8.80365 3.53109 9.0538 3.28094 9.0538 2.97273C9.0538 2.76725 8.93766 2.57517 8.75452 2.48137L5.22568 0.623142C4.9666 0.484669 4.65391 0.484669 4.39484 0.623142V0.623142Z" fill="currentColor"></path></svg>

	<span class="-mr-1 text-gray-400">License:</span>

	<span>mit</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 dark:border-b-gray-700 dark:border-r-gray-700"></div></div>
		
		</button>
	
	
	</div></div>

		<div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden "><a class="tab-alternate active" href="/openai-community/gpt2"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			Model card
			
			
		</a><a class="tab-alternate " href="/openai-community/gpt2/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			<span class="xl:hidden">Files</span>
				<span class="hidden xl:inline">Files and versions</span>
			
			
		</a><a class="tab-alternate " href="/openai-community/gpt2/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
			<div class="ml-1.5 flex h-4 min-w-[1rem] items-center justify-center rounded px-1 text-xs leading-none shadow-sm bg-black text-white dark:bg-gray-800 dark:text-gray-200">93
				</div>
			
		</a>
	</div>
	
			


<div class="relative mb-1.5 flex flex-wrap gap-1.5 sm:flex-nowrap lg:mb-0"><div class="order-last sm:order-first"><div class="relative ">
	<button class="btn px-1.5 py-1.5 " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-0.5" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
		
		</button>
	
	
	</div></div>













	<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12.1 2a9.8 9.8 0 0 0-5.4 1.6l6.4 6.4a2.1 2.1 0 0 1 .2 3a2.1 2.1 0 0 1-3-.2L3.7 6.4A9.84 9.84 0 0 0 2 12.1a10.14 10.14 0 0 0 10.1 10.1a10.9 10.9 0 0 0 2.6-.3l6.7 6.7a5 5 0 0 0 7.1-7.1l-6.7-6.7a10.9 10.9 0 0 0 .3-2.6A10 10 0 0 0 12.1 2zm8 10.1a7.61 7.61 0 0 1-.3 2.1l-.3 1.1l.8.8l6.7 6.7a2.88 2.88 0 0 1 .9 2.1A2.72 2.72 0 0 1 27 27a2.9 2.9 0 0 1-4.2 0l-6.7-6.7l-.8-.8l-1.1.3a7.61 7.61 0 0 1-2.1.3a8.27 8.27 0 0 1-5.7-2.3A7.63 7.63 0 0 1 4 12.1a8.33 8.33 0 0 1 .3-2.2l4.4 4.4a4.14 4.14 0 0 0 5.9.2a4.14 4.14 0 0 0-.2-5.9L10 4.2a6.45 6.45 0 0 1 2-.3a8.27 8.27 0 0 1 5.7 2.3a8.49 8.49 0 0 1 2.4 5.9z" fill="currentColor"></path></svg>
			Train
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
		


		


		

</div>
	<div class="flex-none w-full sm:w-auto"><div class="relative ">
	<button class="text-sm btn btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><rect x="6.34" y="19" width="11.31" height="2" transform="translate(-10.63 14.34) rotate(-45)"></rect><path d="M17,30a1,1,0,0,1-.37-.07,1,1,0,0,1-.62-.79l-1-7,2-.28.75,5.27L21,24.52V17a1,1,0,0,1,.29-.71l4.07-4.07A8.94,8.94,0,0,0,28,5.86V4H26.14a8.94,8.94,0,0,0-6.36,2.64l-4.07,4.07A1,1,0,0,1,15,11H7.48L4.87,14.26l5.27.75-.28,2-7-1a1,1,0,0,1-.79-.62,1,1,0,0,1,.15-1l4-5A1,1,0,0,1,7,9h7.59l3.77-3.78A10.92,10.92,0,0,1,26.14,2H28a2,2,0,0,1,2,2V5.86a10.92,10.92,0,0,1-3.22,7.78L23,17.41V25a1,1,0,0,1-.38.78l-5,4A1,1,0,0,1,17,30Z"></path></svg>
			Deploy
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>
		


		


		


		


		

</div>
	<div class="relative flex-auto sm:flex-none">
	<button class="!from-gray-800 !to-black !text-white !gap-1 !border-gray-800 dark:!border-gray-900  btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 !mr-0.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M28 4H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h8v4H8v2h16v-2h-4v-4h8a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2ZM18 28h-4v-4h4Zm10-6H4V6h24Z"></path></svg>
			Use this model
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div>

</div>
	</div></div></header></div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12 md:flex-1 md:grid-rows-full space-y-4 md:gap-6 "><section class="pt-8 border-gray-100 md:col-span-7 pb-24 relative break-words copiable-code-container"><div class="SVELTE_HYDRATER contents" data-target="UnsafeBanner" data-props="{&quot;classNames&quot;:&quot;mb-6 md:mb-4 mt-0&quot;,&quot;repoId&quot;:&quot;openai-community/gpt2&quot;,&quot;repoType&quot;:&quot;model&quot;}"></div>
				<a class="btn mb-6 text-sm text-gray-600 md:absolute md:-right-6 md:top-0 md:mb-0 md:rounded-r-none md:rounded-t-none md:border-r-0 md:border-t-0 md:border-gray-100 md:bg-none" href="/openai-community/gpt2/edit/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
						Edit model card
					</a>
				
				
					<div class="SVELTE_HYDRATER contents" data-target="RepoCodeCopy" data-props="{}"><div></div></div>
					
					
					
					<div class="relative md:mt-2"><div class="SVELTE_HYDRATER contents" data-target="SideNavigation" data-props="{&quot;titleTree&quot;:[{&quot;id&quot;:&quot;gpt-2&quot;,&quot;label&quot;:&quot;GPT-2&quot;,&quot;children&quot;:[{&quot;id&quot;:&quot;model-description&quot;,&quot;label&quot;:&quot;Model description&quot;,&quot;children&quot;:[],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Model description&quot;},{&quot;id&quot;:&quot;intended-uses--limitations&quot;,&quot;label&quot;:&quot;Intended uses &amp;amp; limitations&quot;,&quot;children&quot;:[{&quot;id&quot;:&quot;how-to-use&quot;,&quot;label&quot;:&quot;How to use&quot;,&quot;children&quot;:[],&quot;isValid&quot;:true,&quot;title&quot;:&quot;How to use&quot;},{&quot;id&quot;:&quot;limitations-and-bias&quot;,&quot;label&quot;:&quot;Limitations and bias&quot;,&quot;children&quot;:[],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Limitations and bias&quot;}],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Intended uses &amp;amp; limitations&quot;},{&quot;id&quot;:&quot;training-data&quot;,&quot;label&quot;:&quot;Training data&quot;,&quot;children&quot;:[],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Training data&quot;},{&quot;id&quot;:&quot;training-procedure&quot;,&quot;label&quot;:&quot;Training procedure&quot;,&quot;children&quot;:[{&quot;id&quot;:&quot;preprocessing&quot;,&quot;label&quot;:&quot;Preprocessing&quot;,&quot;children&quot;:[],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Preprocessing&quot;}],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Training procedure&quot;},{&quot;id&quot;:&quot;evaluation-results&quot;,&quot;label&quot;:&quot;Evaluation results&quot;,&quot;children&quot;:[{&quot;id&quot;:&quot;bibtex-entry-and-citation-info&quot;,&quot;label&quot;:&quot;BibTeX entry and citation info&quot;,&quot;children&quot;:[],&quot;isValid&quot;:true,&quot;title&quot;:&quot;BibTeX entry and citation info&quot;}],&quot;isValid&quot;:true,&quot;title&quot;:&quot;Evaluation results&quot;}],&quot;isValid&quot;:true,&quot;title&quot;:&quot;GPT-2&quot;}]}">

<div class="absolute -left-12 z-10 h-full "><div class="sticky top-4 flex"><div class="pt-[0.175rem]">
				<span class="peer" tabindex="0"><button class="select-none hover:cursor-pointer"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-lg opacity-80 hover:opacity-100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg></button></span>
				<div class="invisible w-0 -translate-x-24 -translate-y-6 overflow-hidden rounded-xl border bg-white transition-transform hover:visible hover:w-52 hover:translate-x-0 peer-focus-within:visible peer-focus-within:w-52 peer-focus-within:translate-x-0"><nav aria-label="Secondary" class="max-h-[550px] overflow-y-auto p-3"><ul><li class="mb-3 text-sm last:mb-0"><a class="mb-1 block break-words font-semibold text-gray-700 hover:underline active:text-gray-900 dark:active:text-gray-200 [&>*]:break-words" href="#gpt-2" title="GPT-2"><!-- HTML_TAG_START -->GPT-2<!-- HTML_TAG_END --></a>
									<ul class="pl-1"><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#model-description" title="Model description"><!-- HTML_TAG_START -->Model description<!-- HTML_TAG_END --></a>
												<ul class="pl-2"></ul>
											</li><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#intended-uses--limitations" title="Intended uses &amp;amp; limitations"><!-- HTML_TAG_START -->Intended uses &amp; limitations<!-- HTML_TAG_END --></a>
												<ul class="pl-2"><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#how-to-use" title="How to use"><!-- HTML_TAG_START -->How to use<!-- HTML_TAG_END --></a>
														</li><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#limitations-and-bias" title="Limitations and bias"><!-- HTML_TAG_START -->Limitations and bias<!-- HTML_TAG_END --></a>
														</li></ul>
											</li><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#training-data" title="Training data"><!-- HTML_TAG_START -->Training data<!-- HTML_TAG_END --></a>
												<ul class="pl-2"></ul>
											</li><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#training-procedure" title="Training procedure"><!-- HTML_TAG_START -->Training procedure<!-- HTML_TAG_END --></a>
												<ul class="pl-2"><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#preprocessing" title="Preprocessing"><!-- HTML_TAG_START -->Preprocessing<!-- HTML_TAG_END --></a>
														</li></ul>
											</li><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#evaluation-results" title="Evaluation results"><!-- HTML_TAG_START -->Evaluation results<!-- HTML_TAG_END --></a>
												<ul class="pl-2"><li><a class="mb-0.5 block break-words hover:underline active:text-gray-700 dark:active:text-gray-300 text-gray-500" href="#bibtex-entry-and-citation-info" title="BibTeX entry and citation info"><!-- HTML_TAG_START -->BibTeX entry and citation info<!-- HTML_TAG_END --></a>
														</li></ul>
											</li></ul>
								</li></ul></nav></div></div></div></div></div>
						
							<div class="SVELTE_HYDRATER contents" data-target="Hydrater" data-props="{&quot;targetSelector&quot;:&quot;.model-card-content&quot;}"></div>
							<div class="model-card-content prose md:px-6 md:-mx-6 lg:-mr-20 lg:pr-20 xl:-mr-24 xl:pr-24 2xl:-mr-36 2xl:pr-36 hf-sanitized hf-sanitized-ZYy3oReU1dtspicd0GVxT">
	<!-- HTML_TAG_START --><h1 class="relative group flex items-center">
	<a rel="nofollow" href="#gpt-2" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="gpt-2">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		GPT-2
	</span>
</h1>
<p>Test the whole generation capabilities here: <a rel="nofollow" href="https://transformer.huggingface.co/doc/gpt2-large">https://transformer.huggingface.co/doc/gpt2-large</a></p>
<p>Pretrained model on English language using a causal language modeling (CLM) objective. It was introduced in
<a rel="nofollow" href="https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf">this paper</a>
and first released at <a rel="nofollow" href="https://openai.com/blog/better-language-models/">this page</a>.</p>
<p>Disclaimer: The team releasing GPT-2 also wrote a
<a rel="nofollow" href="https://github.com/openai/gpt-2/blob/master/model_card.md">model card</a> for their model. Content from this model card
has been written by the Hugging Face team to complete the information they provided and give specific examples of bias.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#model-description" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="model-description">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Model description
	</span>
</h2>
<p>GPT-2 is a transformers model pretrained on a very large corpus of English data in a self-supervised fashion. This
means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots
of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely,
it was trained to guess the next word in sentences.</p>
<p>More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence,
shifted one token (word or piece of word) to the right. The model uses internally a mask-mechanism to make sure the
predictions for the token <code>i</code> only uses the inputs from <code>1</code> to <code>i</code> but not the future tokens.</p>
<p>This way, the model learns an inner representation of the English language that can then be used to extract features
useful for downstream tasks. The model is best at what it was pretrained for however, which is generating texts from a
prompt.</p>
<p>This is the <strong>smallest</strong> version of GPT-2, with 124M parameters. </p>
<p><strong>Related Models:</strong> <a rel="nofollow" href="https://huggingface.co/gpt2-large">GPT-Large</a>, <a rel="nofollow" href="https://huggingface.co/gpt2-medium">GPT-Medium</a> and <a rel="nofollow" href="https://huggingface.co/gpt2-xl">GPT-XL</a></p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#intended-uses--limitations" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="intended-uses--limitations">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Intended uses &amp; limitations
	</span>
</h2>
<p>You can use the raw model for text generation or fine-tune it to a downstream task. See the
<a rel="nofollow" href="https://huggingface.co/models?filter=gpt2">model hub</a> to look for fine-tuned versions on a task that interests you.</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-use" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-use">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to use
	</span>
</h3>
<p>You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we
set a seed for reproducibility:</p>
<pre><code class="language-python"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">from</span> transformers <span class="hljs-keyword">import</span> pipeline, set_seed
<span class="hljs-meta">&gt;&gt;&gt; </span>generator = pipeline(<span class="hljs-string">'text-generation'</span>, model=<span class="hljs-string">'gpt2'</span>)
<span class="hljs-meta">&gt;&gt;&gt; </span>set_seed(<span class="hljs-number">42</span>)
<span class="hljs-meta">&gt;&gt;&gt; </span>generator(<span class="hljs-string">"Hello, I'm a language model,"</span>, max_length=<span class="hljs-number">30</span>, num_return_sequences=<span class="hljs-number">5</span>)

[{<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">"Hello, I'm a language model, a language for thinking, a language for expressing thoughts."</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">"Hello, I'm a language model, a compiler, a compiler library, I just want to know how I build this kind of stuff. I don"</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">"Hello, I'm a language model, and also have more than a few of your own, but I understand that they're going to need some help"</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">"Hello, I'm a language model, a system model. I want to know my language so that it might be more interesting, more user-friendly"</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'Hello, I\'m a language model, not a language model"\n\nThe concept of "no-tricks" comes in handy later with new'</span>}]
</code></pre>
<p>Here is how to use this model to get the features of a given text in PyTorch:</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> transformers <span class="hljs-keyword">import</span> GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained(<span class="hljs-string">'gpt2'</span>)
model = GPT2Model.from_pretrained(<span class="hljs-string">'gpt2'</span>)
text = <span class="hljs-string">"Replace me by any text you'd like."</span>
encoded_input = tokenizer(text, return_tensors=<span class="hljs-string">'pt'</span>)
output = model(**encoded_input)
</code></pre>
<p>and in TensorFlow:</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> transformers <span class="hljs-keyword">import</span> GPT2Tokenizer, TFGPT2Model
tokenizer = GPT2Tokenizer.from_pretrained(<span class="hljs-string">'gpt2'</span>)
model = TFGPT2Model.from_pretrained(<span class="hljs-string">'gpt2'</span>)
text = <span class="hljs-string">"Replace me by any text you'd like."</span>
encoded_input = tokenizer(text, return_tensors=<span class="hljs-string">'tf'</span>)
output = model(encoded_input)
</code></pre>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#limitations-and-bias" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="limitations-and-bias">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Limitations and bias
	</span>
</h3>
<p>The training data used for this model has not been released as a dataset one can browse. We know it contains a lot of
unfiltered content from the internet, which is far from neutral. As the openAI team themselves point out in their
<a rel="nofollow" href="https://github.com/openai/gpt-2/blob/master/model_card.md#out-of-scope-use-cases">model card</a>:</p>
<blockquote>
<p>Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases
that require the generated text to be true.</p>
<p>Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do
not recommend that they be deployed into systems that interact with humans &gt; unless the deployers first carry out a
study of biases relevant to the intended use-case. We found no statistically significant difference in gender, race,
and religious bias probes between 774M and 1.5B, implying all versions of GPT-2 should be approached with similar
levels of caution around use cases that are sensitive to biases around human attributes.</p>
</blockquote>
<p>Here's an example of how the model can have biased predictions:</p>
<pre><code class="language-python"><span class="hljs-meta">&gt;&gt;&gt; </span><span class="hljs-keyword">from</span> transformers <span class="hljs-keyword">import</span> pipeline, set_seed
<span class="hljs-meta">&gt;&gt;&gt; </span>generator = pipeline(<span class="hljs-string">'text-generation'</span>, model=<span class="hljs-string">'gpt2'</span>)
<span class="hljs-meta">&gt;&gt;&gt; </span>set_seed(<span class="hljs-number">42</span>)
<span class="hljs-meta">&gt;&gt;&gt; </span>generator(<span class="hljs-string">"The White man worked as a"</span>, max_length=<span class="hljs-number">10</span>, num_return_sequences=<span class="hljs-number">5</span>)

[{<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The White man worked as a mannequin for'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The White man worked as a maniser of the'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The White man worked as a bus conductor by day'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The White man worked as a plumber at the'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The White man worked as a journalist. He had'</span>}]

<span class="hljs-meta">&gt;&gt;&gt; </span>set_seed(<span class="hljs-number">42</span>)
<span class="hljs-meta">&gt;&gt;&gt; </span>generator(<span class="hljs-string">"The Black man worked as a"</span>, max_length=<span class="hljs-number">10</span>, num_return_sequences=<span class="hljs-number">5</span>)

[{<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The Black man worked as a man at a restaurant'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The Black man worked as a car salesman in a'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The Black man worked as a police sergeant at the'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The Black man worked as a man-eating monster'</span>},
 {<span class="hljs-string">'generated_text'</span>: <span class="hljs-string">'The Black man worked as a slave, and was'</span>}]
</code></pre>
<p>This bias will also affect all fine-tuned versions of this model.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#training-data" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="training-data">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Training data
	</span>
</h2>
<p>The OpenAI team wanted to train this model on a corpus as large as possible. To build it, they scraped all the web
pages from outbound links on Reddit which received at least 3 karma. Note that all Wikipedia pages were removed from
this dataset, so the model was not trained on any part of Wikipedia. The resulting dataset (called WebText) weights
40GB of texts but has not been publicly released. You can find a list of the top 1,000 domains present in WebText
<a rel="nofollow" href="https://github.com/openai/gpt-2/blob/master/domains.txt">here</a>.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#training-procedure" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="training-procedure">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Training procedure
	</span>
</h2>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#preprocessing" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="preprocessing">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Preprocessing
	</span>
</h3>
<p>The texts are tokenized using a byte-level version of Byte Pair Encoding (BPE) (for unicode characters) and a
vocabulary size of 50,257. The inputs are sequences of 1024 consecutive tokens.</p>
<p>The larger model was trained on 256 cloud TPU v3 cores. The training duration was not disclosed, nor were the exact
details of training.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#evaluation-results" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="evaluation-results">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Evaluation results
	</span>
</h2>
<p>The model achieves the following results without any fine-tuning (zero-shot):</p>
<div class="max-w-full overflow-auto">
	<table>
		<thead><tr>
<th align="center">Dataset</th>
<th align="center">LAMBADA</th>
<th align="center">LAMBADA</th>
<th align="center">CBT-CN</th>
<th align="center">CBT-NE</th>
<th align="center">WikiText2</th>
<th align="center">PTB</th>
<th align="center">enwiki8</th>
<th align="center">text8</th>
<th align="center">WikiText103</th>
<th align="center">1BW</th>
</tr>

		</thead><tbody><tr>
<td align="center">(metric)</td>
<td align="center">(PPL)</td>
<td align="center">(ACC)</td>
<td align="center">(ACC)</td>
<td align="center">(ACC)</td>
<td align="center">(PPL)</td>
<td align="center">(PPL)</td>
<td align="center">(BPB)</td>
<td align="center">(BPC)</td>
<td align="center">(PPL)</td>
<td align="center">(PPL)</td>
</tr>
<tr>
<td align="center"></td>
<td align="center">35.13</td>
<td align="center">45.99</td>
<td align="center">87.65</td>
<td align="center">83.4</td>
<td align="center">29.41</td>
<td align="center">65.85</td>
<td align="center">1.16</td>
<td align="center">1,17</td>
<td align="center">37.50</td>
<td align="center">75.20</td>
</tr>
</tbody>
	</table>
</div>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#bibtex-entry-and-citation-info" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="bibtex-entry-and-citation-info">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		BibTeX entry and citation info
	</span>
</h3>
<pre><code class="language-bibtex">@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
</code></pre>
<a href="https://huggingface.co/exbert/?model=gpt2">
    <img src="https://cdn-media.huggingface.co/exbert/button.png" width="300px">
</a>
<!-- HTML_TAG_END --></div>
</div></section>
			<section class="pt-8 border-gray-100 md:col-span-5 pt-6 md:pb-24 md:pl-6 md:border-l order-first md:order-none"><div class="flex justify-between pb-2"><dl><dt class="-mb-1 text-sm text-gray-500">Downloads last month</dt><dd class="font-semibold">6,888,015</dd></dl>
						<div class="model-graph h-[40px] w-[200px] flex-none md:w-[150px] lg:w-[200px]"><!-- HTML_TAG_START -->
			<svg 
				viewbox="0 0 100 100" 
				width="100%" 
				height="100%" 
				preserveAspectRatio="none"
				style="overflow: visible;"
			>
				<defs>
					<linearGradient id="fill-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
						<stop offset="0%" style="stop-color: rgb(137, 86, 255); stop-opacity:0.3" />
						<stop offset="100%" style="stop-color: rgb(137, 86, 255); stop-opacity:0.05" />
					</linearGradient>
				</defs>
				
			<path d="M 0,44.6C 0.2,45 3.1,52 3.4,52.2C 3.7,52.4 6.6,49.9 6.9,49.4C 7.2,48.9 10,44.4 10.3,43.1C 10.6,41.8 13.5,23.2 13.8,23.9C 14.1,24.6 16.9,54.7 17.2,57.4C 17.5,60.1 20.4,77.8 20.7,77C 21,76.2 23.8,44 24.1,40.6C 24.4,37.2 27.3,8.3 27.6,8.6C 27.9,8.9 30.7,44.5 31,45.7C 31.3,46.9 34.2,32.5 34.5,32.5C 34.8,32.5 37.6,44.5 37.9,46.5C 38.2,48.5 41.1,70.9 41.4,72.4C 41.7,73.9 44.5,77.3 44.8,76.9C 45.1,76.5 48,64.7 48.3,64.3C 48.6,63.9 51.4,70.5 51.7,68.6C 52,66.7 54.9,27.6 55.2,25.6C 55.5,23.6 58.3,27.4 58.6,28C 58.9,28.6 61.8,36.2 62.1,38.5C 62.4,40.8 65.2,72 65.5,73.8C 65.8,75.6 68.7,76.5 69,75.4C 69.3,74.3 72.1,52.9 72.4,51.5C 72.7,50.1 75.6,48.1 75.9,48.1C 76.2,48.1 79,50.7 79.3,51.6C 79.6,52.5 82.5,66.2 82.8,67C 83.1,67.8 85.9,66.5 86.2,66.8C 86.5,67.1 89.4,77.2 89.7,73.9C 90,70.6 92.8,0.6 93.1,0C 93.4,-0.6 96.6,61.6 96.6,61.6C 96.6,61.6 99.8,98.1 100,100" 
				fill="none"
				stroke="rgb(137, 86, 255)" 
				stroke-width="3"
				vector-effect="non-scaling-stroke"
			/>
			<path d="M 0,100 L 0,44.6C 0.2,45 3.1,52 3.4,52.2C 3.7,52.4 6.6,49.9 6.9,49.4C 7.2,48.9 10,44.4 10.3,43.1C 10.6,41.8 13.5,23.2 13.8,23.9C 14.1,24.6 16.9,54.7 17.2,57.4C 17.5,60.1 20.4,77.8 20.7,77C 21,76.2 23.8,44 24.1,40.6C 24.4,37.2 27.3,8.3 27.6,8.6C 27.9,8.9 30.7,44.5 31,45.7C 31.3,46.9 34.2,32.5 34.5,32.5C 34.8,32.5 37.6,44.5 37.9,46.5C 38.2,48.5 41.1,70.9 41.4,72.4C 41.7,73.9 44.5,77.3 44.8,76.9C 45.1,76.5 48,64.7 48.3,64.3C 48.6,63.9 51.4,70.5 51.7,68.6C 52,66.7 54.9,27.6 55.2,25.6C 55.5,23.6 58.3,27.4 58.6,28C 58.9,28.6 61.8,36.2 62.1,38.5C 62.4,40.8 65.2,72 65.5,73.8C 65.8,75.6 68.7,76.5 69,75.4C 69.3,74.3 72.1,52.9 72.4,51.5C 72.7,50.1 75.6,48.1 75.9,48.1C 76.2,48.1 79,50.7 79.3,51.6C 79.6,52.5 82.5,66.2 82.8,67C 83.1,67.8 85.9,66.5 86.2,66.8C 86.5,67.1 89.4,77.2 89.7,73.9C 90,70.6 92.8,0.6 93.1,0C 93.4,-0.6 96.6,61.6 96.6,61.6C 96.6,61.6 99.8,98.1 100,100 L 100,100"
				fill="url(#fill-gradient)"
				stroke="none" 
				vector-effect="non-scaling-stroke"
			/>
		
			</svg>
		<!-- HTML_TAG_END --></div></div>
					<div class="divider-column-vertical"></div>

				<div class="SVELTE_HYDRATER contents" data-target="ModelTensorsParams" data-props="{&quot;modelId&quot;:&quot;openai-community/gpt2&quot;,&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;F32&quot;:137022720},&quot;total&quot;:137022720,&quot;sharded&quot;:false},&quot;isGated&quot;:false,&quot;query&quot;:{},&quot;model&quot;:{&quot;author&quot;:&quot;openai-community&quot;,&quot;cardData&quot;:{&quot;language&quot;:&quot;en&quot;,&quot;tags&quot;:[&quot;exbert&quot;],&quot;license&quot;:&quot;mit&quot;},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;architectures&quot;:[&quot;GPT2LMHeadModel&quot;],&quot;model_type&quot;:&quot;gpt2&quot;,&quot;tokenizer_config&quot;:{}},&quot;createdAt&quot;:&quot;2022-03-02T23:29:04.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;downloads&quot;:6888015,&quot;downloadsAllTime&quot;:592183811,&quot;doi&quot;:{&quot;id&quot;:&quot;10.57967/hf/0039&quot;,&quot;commit&quot;:&quot;909a290700bd99135e67c64eefc166960b67cfd2&quot;},&quot;id&quot;:&quot;openai-community/gpt2&quot;,&quot;isLikedByUser&quot;:false,&quot;isWatchedByUser&quot;:false,&quot;inference&quot;:&quot;Yes&quot;,&quot;lastModified&quot;:&quot;2024-02-19T10:57:45.000Z&quot;,&quot;likes&quot;:2076,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;pwcLink&quot;:{&quot;error&quot;:&quot;Unknown error, can't generate link to Papers With Code.&quot;},&quot;tags&quot;:[&quot;transformers&quot;,&quot;pytorch&quot;,&quot;tf&quot;,&quot;jax&quot;,&quot;tflite&quot;,&quot;rust&quot;,&quot;onnx&quot;,&quot;safetensors&quot;,&quot;gpt2&quot;,&quot;text-generation&quot;,&quot;exbert&quot;,&quot;en&quot;,&quot;doi:10.57967/hf/0039&quot;,&quot;license:mit&quot;,&quot;autotrain_compatible&quot;,&quot;text-generation-inference&quot;,&quot;endpoints_compatible&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;text-generation&quot;,&quot;label&quot;:&quot;Text Generation&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;nlp&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;pytorch&quot;,&quot;label&quot;:&quot;PyTorch&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tf&quot;,&quot;label&quot;:&quot;TensorFlow&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;jax&quot;,&quot;label&quot;:&quot;JAX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tflite&quot;,&quot;label&quot;:&quot;TF Lite&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;rust&quot;,&quot;label&quot;:&quot;Rust&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;onnx&quot;,&quot;label&quot;:&quot;ONNX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;safetensors&quot;,&quot;label&quot;:&quot;Safetensors&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;en&quot;,&quot;label&quot;:&quot;English&quot;,&quot;type&quot;:&quot;language&quot;},{&quot;id&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;label&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;type&quot;:&quot;doi&quot;},{&quot;id&quot;:&quot;gpt2&quot;,&quot;label&quot;:&quot;gpt2&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;exbert&quot;,&quot;label&quot;:&quot;exbert&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;autotrain_compatible&quot;,&quot;label&quot;:&quot;AutoTrain Compatible&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;text-generation-inference&quot;,&quot;label&quot;:&quot;text-generation-inference&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;endpoints_compatible&quot;,&quot;label&quot;:&quot;Inference Endpoints&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;license:mit&quot;,&quot;label&quot;:&quot;mit&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModelForCausalLM&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;processor&quot;:&quot;AutoTokenizer&quot;},&quot;widgetData&quot;:[{&quot;text&quot;:&quot;My name is Julien and I like to&quot;},{&quot;text&quot;:&quot;My name is Thomas and my main&quot;},{&quot;text&quot;:&quot;My name is Mariama, my favorite&quot;},{&quot;text&quot;:&quot;My name is Clara and I am&quot;},{&quot;text&quot;:&quot;My name is Lewis and I like to&quot;},{&quot;text&quot;:&quot;My name is Merve and my favorite&quot;},{&quot;text&quot;:&quot;My name is Teven and I am&quot;},{&quot;text&quot;:&quot;Once upon a time,&quot;}],&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;F32&quot;:137022720},&quot;total&quot;:137022720,&quot;sharded&quot;:false},&quot;inferenceLoadInfo&quot;:{&quot;compute_type&quot;:&quot;cpu&quot;,&quot;state&quot;:&quot;Loadable&quot;},&quot;inferenceStatus&quot;:&quot;loaded&quot;}}"><div class="flex gap-1.5 flex-wrap"><div class="mr-auto flex flex-none items-center gap-1 overflow-hidden rounded-lg text-smd font-semibold"><svg class="" viewBox="0 0 57 44" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet"><path d="M36.816 20.1474L54.9918 27.4409C55.5142 27.6506 55.9623 28.0112 56.2788 28.4766C56.5954 28.9421 56.7661 29.4913 56.7691 30.0542C56.7722 30.6171 56.6074 31.1682 56.2959 31.637C55.9844 32.1059 55.5402 32.4713 55.0201 32.6866L29.953 43.0646C29.2593 43.3518 28.4799 43.3518 27.7862 43.0646L2.71624 32.6894C2.19613 32.4741 1.75197 32.1087 1.44044 31.6398C1.12892 31.171 0.964165 30.62 0.967204 30.057C0.970244 29.4941 1.14094 28.9449 1.45751 28.4794C1.77408 28.014 2.22216 27.6534 2.74456 27.4437L21.2404 20.0227C22.2997 19.5979 25.6477 20.8441 28.8682 20.8555C32.3096 20.8668 35.6292 19.6715 36.816 20.1474ZM11.3042 30.1119L28.8682 37.3828L46.435 30.1119L28.8682 23.0619L11.3042 30.1119ZM29.9247 0.388251L54.9918 10.4462C55.5142 10.6559 55.9623 11.0165 56.2788 11.482C56.5954 11.9474 56.7661 12.4967 56.7691 13.0596C56.7722 13.6225 56.6074 14.1735 56.2959 14.6424C55.9844 15.1112 55.5402 15.4766 55.0201 15.6919L29.953 26.07C29.2593 26.3572 28.4799 26.3572 27.7862 26.07L2.71624 15.6948C2.19613 15.4795 1.75197 15.1141 1.44044 14.6452C1.12892 14.1763 0.964165 13.6253 0.967204 13.0624C0.970244 12.4995 1.14094 11.9503 1.45751 11.4848C1.77408 11.0193 2.22216 10.6588 2.74456 10.4491L27.8117 0.388251C28.4896 0.1157 29.2467 0.1157 29.9247 0.388251ZM11.3042 13.1172L28.8682 20.3881L46.435 13.1172L28.8682 6.06729L11.3042 13.1172Z" fill="currentColor"></path></svg>Safetensors<a target="_blank" href="https://huggingface.co/docs/safetensors" class="flex-none text-xs text-gray-400 hover:text-gray-500"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M17 22v-8h-4v2h2v6h-3v2h8v-2h-3z" fill="currentColor"></path><path d="M16 8a1.5 1.5 0 1 0 1.5 1.5A1.5 1.5 0 0 0 16 8z" fill="currentColor"></path><path d="M16 30a14 14 0 1 1 14-14a14 14 0 0 1-14 14zm0-26a12 12 0 1 0 12 12A12 12 0 0 0 16 4z" fill="currentColor"></path></svg></a></div>
		<div class="flex flex-wrap gap-x-1.5 gap-y-1 text-sm"><div class="inline-flex h-6 shrink-0 items-center overflow-hidden rounded-lg border"><div class="border-r px-2 text-gray-500">Model size</div>
				<div class="px-1.5">137M params</div></div>
			<div class="inline-flex h-6 shrink-0 items-center overflow-hidden rounded-lg border"><div class="border-r px-2 text-gray-500">Tensor type</div>
				<div class="flex px-1.5">F32
						<div class="mx-1 text-gray-400 last:hidden">·</div></div></div>
			<button class="from-gray-50-to-white inline-flex h-6 w-6 items-center justify-center overflow-hidden rounded-lg border bg-gradient-to-t hover:shadow-inner dark:hover:brightness-125" title="" ><svg class="text-xs" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path fill="currentColor" d="M10 6v2h12.59L6 24.59L7.41 26L24 9.41V22h2V6H10z"></path></svg></button></div></div>

</div>
					<div class="divider-column-vertical"></div>

				<div class="bg-white pb-1"><div class="SVELTE_HYDRATER contents" data-target="InferenceWidget" data-props="{&quot;apiUrl&quot;:&quot;https://api-inference.huggingface.co&quot;,&quot;model&quot;:{&quot;author&quot;:&quot;openai-community&quot;,&quot;cardData&quot;:{&quot;language&quot;:&quot;en&quot;,&quot;tags&quot;:[&quot;exbert&quot;],&quot;license&quot;:&quot;mit&quot;},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;architectures&quot;:[&quot;GPT2LMHeadModel&quot;],&quot;model_type&quot;:&quot;gpt2&quot;,&quot;tokenizer_config&quot;:{}},&quot;createdAt&quot;:&quot;2022-03-02T23:29:04.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;downloads&quot;:6888015,&quot;downloadsAllTime&quot;:592183811,&quot;doi&quot;:{&quot;id&quot;:&quot;10.57967/hf/0039&quot;,&quot;commit&quot;:&quot;909a290700bd99135e67c64eefc166960b67cfd2&quot;},&quot;id&quot;:&quot;openai-community/gpt2&quot;,&quot;isLikedByUser&quot;:false,&quot;isWatchedByUser&quot;:false,&quot;inference&quot;:&quot;Yes&quot;,&quot;lastModified&quot;:&quot;2024-02-19T10:57:45.000Z&quot;,&quot;likes&quot;:2076,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;pwcLink&quot;:{&quot;error&quot;:&quot;Unknown error, can't generate link to Papers With Code.&quot;},&quot;tags&quot;:[&quot;transformers&quot;,&quot;pytorch&quot;,&quot;tf&quot;,&quot;jax&quot;,&quot;tflite&quot;,&quot;rust&quot;,&quot;onnx&quot;,&quot;safetensors&quot;,&quot;gpt2&quot;,&quot;text-generation&quot;,&quot;exbert&quot;,&quot;en&quot;,&quot;doi:10.57967/hf/0039&quot;,&quot;license:mit&quot;,&quot;autotrain_compatible&quot;,&quot;text-generation-inference&quot;,&quot;endpoints_compatible&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;text-generation&quot;,&quot;label&quot;:&quot;Text Generation&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;nlp&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;pytorch&quot;,&quot;label&quot;:&quot;PyTorch&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tf&quot;,&quot;label&quot;:&quot;TensorFlow&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;jax&quot;,&quot;label&quot;:&quot;JAX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tflite&quot;,&quot;label&quot;:&quot;TF Lite&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;rust&quot;,&quot;label&quot;:&quot;Rust&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;onnx&quot;,&quot;label&quot;:&quot;ONNX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;safetensors&quot;,&quot;label&quot;:&quot;Safetensors&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;en&quot;,&quot;label&quot;:&quot;English&quot;,&quot;type&quot;:&quot;language&quot;},{&quot;id&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;label&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;type&quot;:&quot;doi&quot;},{&quot;id&quot;:&quot;gpt2&quot;,&quot;label&quot;:&quot;gpt2&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;exbert&quot;,&quot;label&quot;:&quot;exbert&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;autotrain_compatible&quot;,&quot;label&quot;:&quot;AutoTrain Compatible&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;text-generation-inference&quot;,&quot;label&quot;:&quot;text-generation-inference&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;endpoints_compatible&quot;,&quot;label&quot;:&quot;Inference Endpoints&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;license:mit&quot;,&quot;label&quot;:&quot;mit&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModelForCausalLM&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;processor&quot;:&quot;AutoTokenizer&quot;},&quot;widgetData&quot;:[{&quot;text&quot;:&quot;My name is Julien and I like to&quot;},{&quot;text&quot;:&quot;My name is Thomas and my main&quot;},{&quot;text&quot;:&quot;My name is Mariama, my favorite&quot;},{&quot;text&quot;:&quot;My name is Clara and I am&quot;},{&quot;text&quot;:&quot;My name is Lewis and I like to&quot;},{&quot;text&quot;:&quot;My name is Merve and my favorite&quot;},{&quot;text&quot;:&quot;My name is Teven and I am&quot;},{&quot;text&quot;:&quot;Once upon a time,&quot;}],&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;F32&quot;:137022720},&quot;total&quot;:137022720,&quot;sharded&quot;:false},&quot;inferenceLoadInfo&quot;:{&quot;compute_type&quot;:&quot;cpu&quot;,&quot;state&quot;:&quot;Loadable&quot;},&quot;inferenceStatus&quot;:&quot;loaded&quot;},&quot;shouldUpdateUrl&quot;:true,&quot;includeCredentials&quot;:true,&quot;isLoggedIn&quot;:false,&quot;callApiOnMount&quot;:true}"><form class="flex w-full max-w-full flex-col ">
		<div class="mb-2 flex items-center font-semibold"><div class="flex items-center text-lg"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" class="-ml-1 mr-1 text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M11 15H6l7-14v8h5l-7 14v-8z" fill="currentColor"></path></svg>
					Inference API</div>
			<a target="_blank" href="https://huggingface.co/docs/hub/models-widgets#example-outputs"><svg class="ml-1.5 text-sm text-gray-400 hover:text-black" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M17 22v-8h-4v2h2v6h-3v2h8v-2h-3z" fill="currentColor"></path><path d="M16 8a1.5 1.5 0 1 0 1.5 1.5A1.5 1.5 0 0 0 16 8z" fill="currentColor"></path><path d="M16 30a14 14 0 1 1 14-14a14 14 0 0 1-14 14zm0-26a12 12 0 1 0 12 12A12 12 0 0 0 16 4z" fill="currentColor"></path></svg></a></div>
<div class="mb-0.5 flex w-full max-w-full flex-wrap items-center text-sm text-gray-500"><div class="flex gap-4 items-center mb-1.5"><a href="/tasks/text-generation" target="_blank" title="Learn more about text-generation"><div class="inline-flex items-center hover:underline"><svg class="mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 18 18"><path d="M16.2607 8.08202L14.468 6.28928C14.3063 6.12804 14.0873 6.03749 13.859 6.03749C13.6307 6.03749 13.4117 6.12804 13.25 6.28928L5.6375 13.904V16.9125H8.64607L16.2607 9.30002C16.422 9.13836 16.5125 8.91935 16.5125 8.69102C16.5125 8.4627 16.422 8.24369 16.2607 8.08202V8.08202ZM8.1953 15.825H6.725V14.3547L11.858 9.22118L13.3288 10.6915L8.1953 15.825ZM14.0982 9.92262L12.6279 8.45232L13.8606 7.21964L15.3309 8.68994L14.0982 9.92262Z"></path><path d="M6.18125 9.84373H7.26875V6.03748H8.9V4.94998H4.55V6.03748H6.18125V9.84373Z"></path><path d="M4.55 11.475H2.375V2.775H11.075V4.95H12.1625V2.775C12.1625 2.48658 12.0479 2.20997 11.844 2.00602C11.64 1.80208 11.3634 1.6875 11.075 1.6875H2.375C2.08658 1.6875 1.80997 1.80208 1.60602 2.00602C1.40207 2.20997 1.2875 2.48658 1.2875 2.775V11.475C1.2875 11.7634 1.40207 12.04 1.60602 12.244C1.80997 12.4479 2.08658 12.5625 2.375 12.5625H4.55V11.475Z"></path></svg>
	<span>Text Generation</span></div></a></div>

	<div class="flex gap-2 ml-auto">
		

<div class="flex gap-x-1 peer:">
	

	
	<div class="relative mb-1.5  ">
		<div class="inline-flex w-32 justify-between rounded-md border border-gray-100 px-4 py-1"><div class="truncate text-sm">Examples</div>
			<svg class="-mr-1 ml-2 h-5 w-5 transition ease-in-out transform false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg></div>

		</div></div></div></div>
	<div class="space-y-2"><div class=""><label class="block ">
	
	
			<span class="block w-full resize-y overflow-auto py-2 px-3 min-h-[144px] inline-block max-h-[500px] whitespace-pre-wrap rounded-lg border border-gray-200 shadow-inner outline-none focus:shadow-inner focus:ring focus:ring-blue-200 dark:bg-gray-925 svelte-1wfa7x9" role="textbox" style="--placeholder: 'Your sentence here...'" spellcheck="false" dir="auto" contenteditable></span></label></div>


		
		<div class="flex items-center gap-x-2 "><div class=""><button class="btn-widget h-10 w-24 px-5 "  type="submit">Compute</button></div>


			<kbd class="hidden rounded border border-gray-200 bg-gray-100 py-0.5 px-1.5 text-xs leading-none text-gray-700 dark:bg-gray-800 dark:text-gray-300 md:inline opacity-70"></kbd>
			<div class="ml-auto self-start"></div></div>
		
		</div>
	<div class="mt-2"><div class="text-xs text-gray-400"><!-- HTML_TAG_START -->This model can be loaded on Inference API (serverless).<!-- HTML_TAG_END --></div>
	
	</div>

	

	<div class="mt-auto flex items-center pt-4 text-xs text-gray-500"><button class="flex items-center cursor-not-allowed text-gray-300" disabled type="button"><svg class="mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
			JSON Output
		</button>
	<div class="ml-auto"><button class="flex items-center" type="button"><svg class="mr-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M22 16h2V8h-8v2h6v6z" fill="currentColor"></path><path d="M8 24h8v-2h-6v-6H8v8z" fill="currentColor"></path><path d="M26 28H6a2.002 2.002 0 0 1-2-2V6a2.002 2.002 0 0 1 2-2h20a2.002 2.002 0 0 1 2 2v20a2.002 2.002 0 0 1-2 2zM6 6v20h20.001L26 6z" fill="currentColor"></path></svg>
			Maximize</button></div>

</div>
</form></div></div>

				
				
				<div class="divider-column-vertical"></div>
					<h2 class="mb-5 flex items-baseline overflow-hidden whitespace-nowrap text-smd font-semibold text-gray-800"><svg class="mr-1 inline self-center flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M7.80914 18.7462V24.1907H13.2536V18.7462H7.80914Z" fill="#FF3270"></path><path d="M18.7458 18.7462V24.1907H24.1903V18.7462H18.7458Z" fill="#861FFF"></path><path d="M7.80914 7.80982V13.2543H13.2536V7.80982H7.80914Z" fill="#097EFF"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4 6.41775C4 5.08246 5.08246 4 6.41775 4H14.6457C15.7626 4 16.7026 4.75724 16.9802 5.78629C18.1505 4.67902 19.7302 4 21.4685 4C25.0758 4 28.0003 6.92436 28.0003 10.5317C28.0003 12.27 27.3212 13.8497 26.2139 15.02C27.243 15.2977 28.0003 16.2376 28.0003 17.3545V25.5824C28.0003 26.9177 26.9177 28.0003 25.5824 28.0003H17.0635H14.9367H6.41775C5.08246 28.0003 4 26.9177 4 25.5824V15.1587V14.9367V6.41775ZM7.80952 7.80952V13.254H13.254V7.80952H7.80952ZM7.80952 24.1907V18.7462H13.254V24.1907H7.80952ZM18.7462 24.1907V18.7462H24.1907V24.1907H18.7462ZM18.7462 10.5317C18.7462 9.0283 19.9651 7.80952 21.4685 7.80952C22.9719 7.80952 24.1907 9.0283 24.1907 10.5317C24.1907 12.0352 22.9719 13.254 21.4685 13.254C19.9651 13.254 18.7462 12.0352 18.7462 10.5317Z" fill="black"></path><path d="M21.4681 7.80982C19.9647 7.80982 18.7458 9.02861 18.7458 10.5321C18.7458 12.0355 19.9647 13.2543 21.4681 13.2543C22.9715 13.2543 24.1903 12.0355 24.1903 10.5321C24.1903 9.02861 22.9715 7.80982 21.4681 7.80982Z" fill="#FFD702"></path></svg>
						Spaces using
						<span class="ml-1 truncate font-mono text-[0.86rem] font-medium">openai-community/gpt2</span>
						<span class="ml-3 font-normal text-gray-400">100</span></h2>
					<div class="SVELTE_HYDRATER contents" data-target="LinkedSpacesList" data-props="{&quot;linkedSpaces&quot;:[{&quot;emoji&quot;:&quot;🏆&quot;,&quot;id&quot;:&quot;open-llm-leaderboard/open_llm_leaderboard&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;Track, rank and evaluate open LLMs and chatbots&quot;},{&quot;emoji&quot;:&quot;😻&quot;,&quot;id&quot;:&quot;microsoft/HuggingGPT&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;😻&quot;,&quot;id&quot;:&quot;Gustavosta/MagicPrompt-Stable-Diffusion&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;shi-labs/Versatile-Diffusion&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🏆🏋️&quot;,&quot;id&quot;:&quot;optimum/llm-perf-leaderboard&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📚&quot;,&quot;id&quot;:&quot;h2oai/h2ogpt-chatbot&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;microsoft/Promptist&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📚&quot;,&quot;id&quot;:&quot;yizhangliu/Grounded-Segment-Anything&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🦾&quot;,&quot;id&quot;:&quot;aliabid94/AutoGPT&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🐢&quot;,&quot;id&quot;:&quot;Manmay/tortoise-tts&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;ExpressivText-to-Speech &quot;},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;wangrongsheng/ChatPaper&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📚&quot;,&quot;id&quot;:&quot;h2oai/h2ogpt-chatbot2&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🖼&quot;,&quot;id&quot;:&quot;OFA-Sys/OFA-Image_Caption&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🏆&quot;,&quot;id&quot;:&quot;Intel/low_bit_open_llm_leaderboard&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;Track, rank and evaluate open LLMs and chatbots&quot;},{&quot;emoji&quot;:&quot;🏃&quot;,&quot;id&quot;:&quot;OpenMotionLab/MotionGPT&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;💩&quot;,&quot;id&quot;:&quot;ShiwenNi/ChatReviewer&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🏆&quot;,&quot;id&quot;:&quot;eduagarcia/open_pt_llm_leaderboard&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;Track, rank and evaluate open LLMs in Portuguese&quot;},{&quot;emoji&quot;:&quot;✍👀&quot;,&quot;id&quot;:&quot;m-ric/beam_search_visualizer&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;View how beam search decoding works, in detail!&quot;},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;exbert-project/exbert&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;😻😻&quot;,&quot;id&quot;:&quot;doevent/Stable-Diffusion-prompt-generator&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🖼️&quot;,&quot;id&quot;:&quot;flax-community/image-captioning&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🧙🏼‍♂️&quot;,&quot;id&quot;:&quot;treadon/prompt-fungineer-355M&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🏔️&quot;,&quot;id&quot;:&quot;open-llm-leaderboard/blog&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;SeaLLMs/SeaLLM-7B&quot;,&quot;running&quot;:false,&quot;shortDescription&quot;:&quot;Multilingual MultiModal Model for SEA&quot;},{&quot;emoji&quot;:&quot;🎦📝&quot;,&quot;id&quot;:&quot;nateraw/lavila&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;👀&quot;,&quot;id&quot;:&quot;yizhangliu/Text-to-Image&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🏆&quot;,&quot;id&quot;:&quot;BAAI/open_cn_llm_leaderboard&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🏆&quot;,&quot;id&quot;:&quot;gsaivinay/open_llm_leaderboard&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🎬&quot;,&quot;id&quot;:&quot;deepklarity/poster2plot&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🌋&quot;,&quot;id&quot;:&quot;EleutherAI/magma&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;💩&quot;,&quot;id&quot;:&quot;akhaliq/CLIP_prefix_captioning&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🦀&quot;,&quot;id&quot;:&quot;FrankZxShen/so-vits-svc-models-ba&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;👀&quot;,&quot;id&quot;:&quot;OFA-Sys/OFA-Visual_Grounding&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🏃&quot;,&quot;id&quot;:&quot;maxmax20160403/sovits5.0&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🎓&quot;,&quot;id&quot;:&quot;OFA-Sys/OFA-vqa&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🏃&quot;,&quot;id&quot;:&quot;Gustavosta/MagicPrompt-Dalle&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🍄&quot;,&quot;id&quot;:&quot;phenomenon1981/MagicPrompt-Stable-Diffusion&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;TMElyralab/MuseTalk&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;OFA-Sys/OFA-Generic_Interface&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🖼📝&quot;,&quot;id&quot;:&quot;johko/capdec-image-captioning&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🐠&quot;,&quot;id&quot;:&quot;ShiwenNi/ChatResponse&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🔗&quot;,&quot;id&quot;:&quot;hkunlp/Binder&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;⌨&quot;,&quot;id&quot;:&quot;aubmindlab/Arabic-NLP&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;bipin/image2story&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;✨&quot;,&quot;id&quot;:&quot;LilyF/Generate_Text_and_Audio&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🏃&quot;,&quot;id&quot;:&quot;Omnibus/Chatbot-Compare&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📉&quot;,&quot;id&quot;:&quot;society-ethics/model-card-regulatory-check&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;📚&quot;,&quot;id&quot;:&quot;Catmeow/AI_story_writing&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🐢&quot;,&quot;id&quot;:&quot;hahahafofo/image2text_prompt_generator&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;ICML2022/OFA&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;📖&quot;,&quot;id&quot;:&quot;thirdai/BOLT2.5B&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🐨&quot;,&quot;id&quot;:&quot;SeaLLMs/SeaLLM-Chat&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;Multilingual ChatBot for SEA Languages&quot;},{&quot;emoji&quot;:&quot;🦀&quot;,&quot;id&quot;:&quot;FrankZxShen/so-vits-svc-models-pcr&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;mshukor/UnIVAL&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🔥&quot;,&quot;id&quot;:&quot;sohaibcs1/Image-to-Text-Summary&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;aliabid94/GPT-Golf&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📈&quot;,&quot;id&quot;:&quot;Hello-SimpleAI/chatgpt-detector-ling&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🐢&quot;,&quot;id&quot;:&quot;llizhx/TinyGPT-V&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🔥&quot;,&quot;id&quot;:&quot;RitaParadaRamos/SmallCapDemo&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;💻&quot;,&quot;id&quot;:&quot;architext/Architext_deployed&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🌍&quot;,&quot;id&quot;:&quot;kmacdermid/RpgRoomGenerator&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;⛓️&quot;,&quot;id&quot;:&quot;SeViLA/SeViLA&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🐠&quot;,&quot;id&quot;:&quot;sasha/BiasDetection&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;⚖&quot;,&quot;id&quot;:&quot;AnimaLab/bias-test-gpt-pairs&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🔊⏫&quot;,&quot;id&quot;:&quot;Nick088/Audio-SR&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;Fixed fork of the original audio sr!&quot;},{&quot;emoji&quot;:&quot;🏃&quot;,&quot;id&quot;:&quot;stanfordnlp/Backpack-Demo&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🐑 🐑&quot;,&quot;id&quot;:&quot;gsarti/pecore&quot;,&quot;running&quot;:true,&quot;shortDescription&quot;:&quot;Analyze context usage in LM generations with model internals&quot;},{&quot;emoji&quot;:&quot;😻&quot;,&quot;id&quot;:&quot;GTBench/GTBench&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;👁&quot;,&quot;id&quot;:&quot;sasha/WinoBiasCheck&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🍹&quot;,&quot;id&quot;:&quot;ccolas/TastyPiano&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;😻&quot;,&quot;id&quot;:&quot;BoomerangGirl/MagicPrompt-Stable-Diffusion&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;💻&quot;,&quot;id&quot;:&quot;dromerosm/gpt-info-extraction&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;📊&quot;,&quot;id&quot;:&quot;hahahafofo/prompt_generator&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;⚡&quot;,&quot;id&quot;:&quot;liyucheng/selective_context&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;💠&quot;,&quot;id&quot;:&quot;zeno-ml/chatbot-report&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📝&quot;,&quot;id&quot;:&quot;lfoppiano/document-qa&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🤷 ➡️ 🤗&quot;,&quot;id&quot;:&quot;Hellisotherpeople/HF-SHAP&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🐠&quot;,&quot;id&quot;:&quot;ethzanalytics/gpt2-xl-conversational&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🎐&quot;,&quot;id&quot;:&quot;taesiri/HuggingGPT-Lite&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🐨&quot;,&quot;id&quot;:&quot;shangdatalab-ucsd/LDB&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;📚&quot;,&quot;id&quot;:&quot;Guinnessgshep/AI_story_writing&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;👀&quot;,&quot;id&quot;:&quot;taka-yamakoshi/tokenizer-demo&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;👀&quot;,&quot;id&quot;:&quot;autonomous019/image_story_generator&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;luis112/text-generation-webui&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🐨&quot;,&quot;id&quot;:&quot;SeaLLMs/SeaLLM-7B-v2&quot;,&quot;running&quot;:false,&quot;shortDescription&quot;:&quot;Multilingual Language Model for SEA&quot;},{&quot;emoji&quot;:&quot;📊&quot;,&quot;id&quot;:&quot;gagan3012/ViTGPT2&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;⚡&quot;,&quot;id&quot;:&quot;yhavinga/dutch-tokenizer-arena&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🔥&quot;,&quot;id&quot;:&quot;abdullahmeda/detect-ai-text&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🐧&quot;,&quot;id&quot;:&quot;ehristoforu/Rensor&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🔥&quot;,&quot;id&quot;:&quot;BigSalmon/InformalToFormal&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;📈&quot;,&quot;id&quot;:&quot;alistairmcleay/cambridge-masters-project&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;📊&quot;,&quot;id&quot;:&quot;codeparrot/apps_metric&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;💻&quot;,&quot;id&quot;:&quot;Catmeow/Text_Generation_Fine_Tune&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;😻&quot;,&quot;id&quot;:&quot;j43fer/MagicPrompt-Stable-Diffusion&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🍄&quot;,&quot;id&quot;:&quot;Daniton/MagicPrompt-Stable-Diffusion&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🏢&quot;,&quot;id&quot;:&quot;ashhadahsan/ai-book-generator&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🌖&quot;,&quot;id&quot;:&quot;Chakshu123/sketch-colorization-with-hint&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;💠&quot;,&quot;id&quot;:&quot;koajoel/PolyFormer&quot;,&quot;running&quot;:true},{&quot;emoji&quot;:&quot;🏆&quot;,&quot;id&quot;:&quot;felixz/open_llm_leaderboard&quot;,&quot;running&quot;:false},{&quot;emoji&quot;:&quot;🚀&quot;,&quot;id&quot;:&quot;xzuyn/Token-Count-Comparison&quot;,&quot;running&quot;:true}]}"><nav class="flex max-w-full flex-wrap gap-x-2.5 gap-y-2"><a href="/spaces/open-llm-leaderboard/open_llm_leaderboard" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  "><div class="mr-2 flex-none text-[0.6rem]">🏆</div>
	<div class="truncate group-hover:underline">open-llm-leaderboard/open_llm_leaderboard</div></a><a href="/spaces/Gustavosta/MagicPrompt-Stable-Diffusion" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  "><div class="mr-2 flex-none text-[0.6rem]">😻</div>
	<div class="truncate group-hover:underline">Gustavosta/MagicPrompt-Stable-Diffusion</div></a><a href="/spaces/shi-labs/Versatile-Diffusion" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  "><div class="mr-2 flex-none text-[0.6rem]">🚀</div>
	<div class="truncate group-hover:underline">shi-labs/Versatile-Diffusion</div></a><a href="/spaces/optimum/llm-perf-leaderboard" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  "><div class="mr-2 flex-none text-[0.6rem]">🏆🏋️</div>
	<div class="truncate group-hover:underline">optimum/llm-perf-leaderboard</div></a><a href="/spaces/microsoft/Promptist" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  "><div class="mr-2 flex-none text-[0.6rem]">🌍</div>
	<div class="truncate group-hover:underline">microsoft/Promptist</div></a><a href="/spaces/yizhangliu/Grounded-Segment-Anything" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">📚</div>
	<div class="truncate group-hover:underline">yizhangliu/Grounded-Segment-Anything</div></a><a href="/spaces/aliabid94/AutoGPT" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🦾</div>
	<div class="truncate group-hover:underline">aliabid94/AutoGPT</div></a><a href="/spaces/Manmay/tortoise-tts" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🐢</div>
	<div class="truncate group-hover:underline">Manmay/tortoise-tts</div></a><a href="/spaces/wangrongsheng/ChatPaper" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🚀</div>
	<div class="truncate group-hover:underline">wangrongsheng/ChatPaper</div></a><a href="/spaces/h2oai/h2ogpt-chatbot2" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">📚</div>
	<div class="truncate group-hover:underline">h2oai/h2ogpt-chatbot2</div></a><a href="/spaces/Intel/low_bit_open_llm_leaderboard" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🏆</div>
	<div class="truncate group-hover:underline">Intel/low_bit_open_llm_leaderboard</div></a><a href="/spaces/ShiwenNi/ChatReviewer" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">💩</div>
	<div class="truncate group-hover:underline">ShiwenNi/ChatReviewer</div></a><a href="/spaces/eduagarcia/open_pt_llm_leaderboard" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🏆</div>
	<div class="truncate group-hover:underline">eduagarcia/open_pt_llm_leaderboard</div></a><a href="/spaces/m-ric/beam_search_visualizer" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">✍👀</div>
	<div class="truncate group-hover:underline">m-ric/beam_search_visualizer</div></a><a href="/spaces/exbert-project/exbert" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🌍</div>
	<div class="truncate group-hover:underline">exbert-project/exbert</div></a><a href="/spaces/doevent/Stable-Diffusion-prompt-generator" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">😻😻</div>
	<div class="truncate group-hover:underline">doevent/Stable-Diffusion-prompt-generator</div></a><a href="/spaces/open-llm-leaderboard/blog" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🏔️</div>
	<div class="truncate group-hover:underline">open-llm-leaderboard/blog</div></a><a href="/spaces/yizhangliu/Text-to-Image" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">👀</div>
	<div class="truncate group-hover:underline">yizhangliu/Text-to-Image</div></a><a href="/spaces/BAAI/open_cn_llm_leaderboard" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🏆</div>
	<div class="truncate group-hover:underline">BAAI/open_cn_llm_leaderboard</div></a><a href="/spaces/FrankZxShen/so-vits-svc-models-ba" class="flex min-w-0 items-center whitespace-nowrap rounded-lg border border-gray-100 px-2 text-xs leading-relaxed text-gray-500 shadow-sm hover:text-gray-800 dark:hover:text-gray-200 md:text-sm md:leading-relaxed  !hidden md:!flex"><div class="mr-2 flex-none text-[0.6rem]">🦀</div>
	<div class="truncate group-hover:underline">FrankZxShen/so-vits-svc-models-ba</div></a>
		<button class="flex items-center rounded-lg border-gray-100 px-2 text-xs leading-relaxed text-gray-600 hover:bg-gray-100 hover:text-gray-600 hover:ring-1 hover:ring-inset hover:ring-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-300 dark:hover:ring-gray-700 md:hidden md:text-sm">+ 95 Spaces
				</button>
			<button class="hidden items-center rounded-lg border-gray-100 px-2 text-xs leading-relaxed text-gray-600 hover:bg-gray-100 hover:text-gray-600 hover:ring-1 hover:ring-inset hover:ring-gray-100 dark:hover:bg-gray-800 dark:hover:text-gray-300 dark:hover:ring-gray-700 md:flex md:text-sm">+ 80 Spaces
				</button></nav></div>
				

				<div class="SVELTE_HYDRATER contents" data-target="ModelEvalResults" data-props="{&quot;model&quot;:{&quot;author&quot;:&quot;openai-community&quot;,&quot;cardData&quot;:{&quot;language&quot;:&quot;en&quot;,&quot;tags&quot;:[&quot;exbert&quot;],&quot;license&quot;:&quot;mit&quot;},&quot;cardExists&quot;:true,&quot;config&quot;:{&quot;architectures&quot;:[&quot;GPT2LMHeadModel&quot;],&quot;model_type&quot;:&quot;gpt2&quot;,&quot;tokenizer_config&quot;:{}},&quot;createdAt&quot;:&quot;2022-03-02T23:29:04.000Z&quot;,&quot;discussionsDisabled&quot;:false,&quot;downloads&quot;:6888015,&quot;downloadsAllTime&quot;:592183811,&quot;doi&quot;:{&quot;id&quot;:&quot;10.57967/hf/0039&quot;,&quot;commit&quot;:&quot;909a290700bd99135e67c64eefc166960b67cfd2&quot;},&quot;id&quot;:&quot;openai-community/gpt2&quot;,&quot;isLikedByUser&quot;:false,&quot;isWatchedByUser&quot;:false,&quot;inference&quot;:&quot;Yes&quot;,&quot;lastModified&quot;:&quot;2024-02-19T10:57:45.000Z&quot;,&quot;likes&quot;:2076,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;library_name&quot;:&quot;transformers&quot;,&quot;librariesOther&quot;:[],&quot;trackDownloads&quot;:true,&quot;model-index&quot;:null,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;gated&quot;:false,&quot;pwcLink&quot;:{&quot;error&quot;:&quot;Unknown error, can't generate link to Papers With Code.&quot;},&quot;tags&quot;:[&quot;transformers&quot;,&quot;pytorch&quot;,&quot;tf&quot;,&quot;jax&quot;,&quot;tflite&quot;,&quot;rust&quot;,&quot;onnx&quot;,&quot;safetensors&quot;,&quot;gpt2&quot;,&quot;text-generation&quot;,&quot;exbert&quot;,&quot;en&quot;,&quot;doi:10.57967/hf/0039&quot;,&quot;license:mit&quot;,&quot;autotrain_compatible&quot;,&quot;text-generation-inference&quot;,&quot;endpoints_compatible&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;text-generation&quot;,&quot;label&quot;:&quot;Text Generation&quot;,&quot;type&quot;:&quot;pipeline_tag&quot;,&quot;subType&quot;:&quot;nlp&quot;},{&quot;id&quot;:&quot;transformers&quot;,&quot;label&quot;:&quot;Transformers&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;pytorch&quot;,&quot;label&quot;:&quot;PyTorch&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tf&quot;,&quot;label&quot;:&quot;TensorFlow&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;jax&quot;,&quot;label&quot;:&quot;JAX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;tflite&quot;,&quot;label&quot;:&quot;TF Lite&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;rust&quot;,&quot;label&quot;:&quot;Rust&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;onnx&quot;,&quot;label&quot;:&quot;ONNX&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;safetensors&quot;,&quot;label&quot;:&quot;Safetensors&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;en&quot;,&quot;label&quot;:&quot;English&quot;,&quot;type&quot;:&quot;language&quot;},{&quot;id&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;label&quot;:&quot;doi:10.57967/hf/0039&quot;,&quot;type&quot;:&quot;doi&quot;},{&quot;id&quot;:&quot;gpt2&quot;,&quot;label&quot;:&quot;gpt2&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;exbert&quot;,&quot;label&quot;:&quot;exbert&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;autotrain_compatible&quot;,&quot;label&quot;:&quot;AutoTrain Compatible&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;text-generation-inference&quot;,&quot;label&quot;:&quot;text-generation-inference&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;endpoints_compatible&quot;,&quot;label&quot;:&quot;Inference Endpoints&quot;,&quot;type&quot;:&quot;other&quot;},{&quot;id&quot;:&quot;license:mit&quot;,&quot;label&quot;:&quot;mit&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;transformersInfo&quot;:{&quot;auto_model&quot;:&quot;AutoModelForCausalLM&quot;,&quot;pipeline_tag&quot;:&quot;text-generation&quot;,&quot;processor&quot;:&quot;AutoTokenizer&quot;},&quot;widgetData&quot;:[{&quot;text&quot;:&quot;My name is Julien and I like to&quot;},{&quot;text&quot;:&quot;My name is Thomas and my main&quot;},{&quot;text&quot;:&quot;My name is Mariama, my favorite&quot;},{&quot;text&quot;:&quot;My name is Clara and I am&quot;},{&quot;text&quot;:&quot;My name is Lewis and I like to&quot;},{&quot;text&quot;:&quot;My name is Merve and my favorite&quot;},{&quot;text&quot;:&quot;My name is Teven and I am&quot;},{&quot;text&quot;:&quot;Once upon a time,&quot;}],&quot;safetensors&quot;:{&quot;parameters&quot;:{&quot;F32&quot;:137022720},&quot;total&quot;:137022720,&quot;sharded&quot;:false},&quot;inferenceLoadInfo&quot;:{&quot;compute_type&quot;:&quot;cpu&quot;,&quot;state&quot;:&quot;Loadable&quot;},&quot;inferenceStatus&quot;:&quot;loaded&quot;}}"></div>
				<div class="divider-column-vertical md:hidden"></div></section></div></main>

	<footer class="b-12 mb-2 flex border-t border-gray-100 md:h-14"><nav class="container flex flex-col justify-between space-y-2 py-6 text-gray-500 md:flex-row md:items-center md:space-y-0 md:py-0 md:text-sm"><div class="font-semibold text-black md:hidden">Company</div>
		<div class="order-last pt-6 text-gray-400 md:order-none md:pt-0" href="Terms">© Hugging Face</div>
		<a class="hover:underline" href="/terms-of-service">TOS</a>
		<a class="hover:underline" href="/privacy">Privacy</a>
		<a class="hover:underline" href="/huggingface">About</a>
		<a class="hover:underline" href="https://apply.workable.com/huggingface/">Jobs</a>
		<a href="/" class="group order-first flex-none pb-6 md:order-none md:pb-0"><svg class="h-7 w-7 transition-transform group-hover:-translate-y-px" viewBox="0 0 95 88" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M47.2119 76.5C66.4037 76.5 81.9619 60.9419 81.9619 41.75C81.9619 22.5581 66.4037 7 47.2119 7C28.02 7 12.4619 22.5581 12.4619 41.75C12.4619 60.9419 28.02 76.5 47.2119 76.5Z" fill="#FFD21E"></path><path d="M81.9619 41.75C81.9619 22.5581 66.4037 7 47.2119 7C28.02 7 12.4619 22.5581 12.4619 41.75C12.4619 60.9419 28.02 76.5 47.2119 76.5C66.4037 76.5 81.9619 60.9419 81.9619 41.75ZM8.46185 41.75C8.46185 20.349 25.8108 3 47.2119 3C68.6129 3 85.9619 20.349 85.9619 41.75C85.9619 63.151 68.6129 80.5 47.2119 80.5C25.8108 80.5 8.46185 63.151 8.46185 41.75Z" fill="#FF9D0B"></path><path d="M58.5024 32.2915C59.7768 32.7415 60.2839 35.3615 61.5713 34.6769C64.0095 33.3805 64.9351 30.353 63.6387 27.9148C62.3423 25.4767 59.3148 24.5511 56.8766 25.8475C54.4384 27.1439 53.5128 30.1714 54.8092 32.6096C55.4211 33.7604 57.3632 31.8892 58.5024 32.2915Z" fill="#3A3B45"></path><path d="M34.9454 32.2915C33.671 32.7415 33.164 35.3615 31.8766 34.6769C29.4384 33.3805 28.5128 30.353 29.8092 27.9148C31.1056 25.4767 34.1331 24.5511 36.5713 25.8475C39.0095 27.1439 39.9351 30.1714 38.6387 32.6096C38.0268 33.7604 36.0846 31.8892 34.9454 32.2915Z" fill="#3A3B45"></path><path d="M46.9619 56.289C56.7903 56.289 59.9619 47.5261 59.9619 43.0262C59.9619 40.6875 58.3898 41.4236 55.8718 42.6702C53.5449 43.8222 50.4102 45.4101 46.9619 45.4101C39.7822 45.4101 33.9619 38.5263 33.9619 43.0262C33.9619 47.5261 37.1334 56.289 46.9619 56.289Z" fill="#3A3B45"></path><mask id="mask0" mask-type="alpha" maskUnits="userSpaceOnUse" x="33" y="41" width="27" height="16"><path d="M46.9619 56.289C56.7903 56.289 59.9619 47.5261 59.9619 43.0262C59.9619 40.6875 58.3898 41.4236 55.8718 42.6702C53.5449 43.8222 50.4102 45.4101 46.9619 45.4101C39.7822 45.4101 33.9619 38.5263 33.9619 43.0262C33.9619 47.5261 37.1334 56.289 46.9619 56.289Z" fill="white"></path></mask><g mask="url(#mask0)"><path d="M47.2119 66.5C52.0018 66.5 55.8848 62.617 55.8848 57.8271C55.8848 54.0962 53.5291 50.9156 50.224 49.6915C50.1023 49.6464 49.9794 49.604 49.8553 49.5643C49.0219 49.2979 48.1337 52.1623 47.2119 52.1623C46.3506 52.1623 45.5186 49.2797 44.7332 49.5135C41.151 50.5799 38.5389 53.8984 38.5389 57.8271C38.5389 62.617 42.4219 66.5 47.2119 66.5Z" fill="#F94040"></path></g><path d="M70.7119 37C72.5068 37 73.9619 35.5449 73.9619 33.75C73.9619 31.9551 72.5068 30.5 70.7119 30.5C68.9169 30.5 67.4619 31.9551 67.4619 33.75C67.4619 35.5449 68.9169 37 70.7119 37Z" fill="#FF9D0B"></path><path d="M24.2119 37C26.0068 37 27.4619 35.5449 27.4619 33.75C27.4619 31.9551 26.0068 30.5 24.2119 30.5C22.4169 30.5 20.9619 31.9551 20.9619 33.75C20.9619 35.5449 22.4169 37 24.2119 37Z" fill="#FF9D0B"></path><path class="origin-bottom-right transition-transform group-hover:-rotate-6" d="M17.5238 48C15.9048 48 14.4578 48.665 13.4488 49.871C12.8248 50.618 12.1728 51.822 12.1198 53.625C11.4408 53.43 10.7878 53.321 10.1778 53.321C8.6278 53.321 7.2278 53.915 6.2378 54.994C4.9658 56.379 4.4008 58.081 4.6468 59.784C4.7638 60.595 5.0348 61.322 5.4398 61.995C4.5858 62.686 3.9568 63.648 3.6528 64.805C3.4148 65.712 3.1708 67.601 4.4448 69.547C4.3638 69.674 4.2878 69.806 4.2168 69.941C3.4508 71.395 3.4018 73.038 4.0778 74.568C5.1028 76.887 7.6498 78.714 12.5958 80.675C15.6728 81.895 18.4878 82.675 18.5128 82.682C22.5808 83.737 26.2598 84.273 29.4448 84.273C35.2988 84.273 39.4898 82.48 41.9018 78.944C45.7838 73.25 45.2288 68.042 40.2058 63.022C37.4258 60.244 35.5778 56.148 35.1928 55.249C34.4168 52.587 32.3648 49.628 28.9538 49.628H28.9528C28.6658 49.628 28.3758 49.651 28.0898 49.696C26.5958 49.931 25.2898 50.791 24.3568 52.085C23.3498 50.833 22.3718 49.837 21.4868 49.275C20.1528 48.429 18.8198 48 17.5238 48ZM17.5238 52C18.0338 52 18.6568 52.217 19.3438 52.653C21.4768 54.006 25.5928 61.081 27.0998 63.833C27.6048 64.755 28.4678 65.145 29.2448 65.145C30.7868 65.145 31.9908 63.612 29.3858 61.664C25.4688 58.733 26.8428 53.942 28.7128 53.647C28.7948 53.634 28.8758 53.628 28.9538 53.628C30.6538 53.628 31.4038 56.558 31.4038 56.558C31.4038 56.558 33.6018 62.078 37.3778 65.851C41.1538 69.625 41.3488 72.654 38.5968 76.69C36.7198 79.442 33.1268 80.273 29.4448 80.273C25.6258 80.273 21.7108 79.379 19.5168 78.81C19.4088 78.782 6.0658 75.013 7.7558 71.805C8.0398 71.266 8.5078 71.05 9.0968 71.05C11.4768 71.05 15.8058 74.592 17.6668 74.592C18.0828 74.592 18.3758 74.415 18.4958 73.983C19.2888 71.138 6.4388 69.942 7.5218 65.821C7.7128 65.092 8.2308 64.796 8.9588 64.797C12.1038 64.797 19.1598 70.328 20.6388 70.328C20.7518 70.328 20.8328 70.295 20.8768 70.225C21.6178 69.029 21.2118 68.194 15.9888 65.033C10.7658 61.871 7.0998 59.969 9.1848 57.699C9.4248 57.437 9.7648 57.321 10.1778 57.321C13.3488 57.322 20.8408 64.14 20.8408 64.14C20.8408 64.14 22.8628 66.243 24.0858 66.243C24.3668 66.243 24.6058 66.132 24.7678 65.858C25.6348 64.396 16.7148 57.636 16.2118 54.847C15.8708 52.957 16.4508 52 17.5238 52Z" fill="#FF9D0B"></path><path class="origin-bottom-right transition-transform group-hover:-rotate-6" d="M38.5967 76.6898C41.3487 72.6538 41.1537 69.6248 37.3777 65.8508C33.6017 62.0778 31.4037 56.5578 31.4037 56.5578C31.4037 56.5578 30.5827 53.3518 28.7127 53.6468C26.8427 53.9418 25.4697 58.7328 29.3867 61.6638C33.3037 64.5938 28.6067 66.5848 27.0997 63.8328C25.5927 61.0808 21.4777 54.0058 19.3437 52.6528C17.2107 51.2998 15.7087 52.0578 16.2117 54.8468C16.7147 57.6358 25.6357 64.3958 24.7677 65.8588C23.8997 67.3208 20.8407 64.1398 20.8407 64.1398C20.8407 64.1398 11.2687 55.4288 9.18465 57.6988C7.10065 59.9688 10.7657 61.8708 15.9887 65.0328C21.2127 68.1938 21.6177 69.0288 20.8767 70.2248C20.1347 71.4208 8.60465 61.6998 7.52165 65.8208C6.43965 69.9418 19.2887 71.1378 18.4957 73.9828C17.7027 76.8288 9.44465 68.5978 7.75565 71.8048C6.06565 75.0128 19.4087 78.7818 19.5167 78.8098C23.8267 79.9278 34.7727 82.2968 38.5967 76.6898Z" fill="#FFD21E"></path><path class="origin-bottom-left transition-transform group-hover:rotate-6" d="M77.3999 48C79.0189 48 80.4659 48.665 81.4749 49.871C82.0989 50.618 82.7509 51.822 82.8039 53.625C83.4829 53.43 84.1359 53.321 84.7459 53.321C86.2959 53.321 87.6959 53.915 88.6859 54.994C89.9579 56.379 90.5229 58.081 90.2769 59.784C90.1599 60.595 89.8889 61.322 89.4839 61.995C90.3379 62.686 90.9669 63.648 91.2709 64.805C91.5089 65.712 91.7529 67.601 90.4789 69.547C90.5599 69.674 90.6359 69.806 90.7069 69.941C91.4729 71.395 91.5219 73.038 90.8459 74.568C89.8209 76.887 87.2739 78.714 82.3279 80.675C79.2509 81.895 76.4359 82.675 76.4109 82.682C72.3429 83.737 68.6639 84.273 65.4789 84.273C59.6249 84.273 55.4339 82.48 53.0219 78.944C49.1399 73.25 49.6949 68.042 54.7179 63.022C57.4979 60.244 59.3459 56.148 59.7309 55.249C60.5069 52.587 62.5589 49.628 65.9699 49.628H65.9709C66.2579 49.628 66.5479 49.651 66.8339 49.696C68.3279 49.931 69.6339 50.791 70.5669 52.085C71.5739 50.833 72.5519 49.837 73.4369 49.275C74.7709 48.429 76.1039 48 77.3999 48ZM77.3999 52C76.8899 52 76.2669 52.217 75.5799 52.653C73.4469 54.006 69.3309 61.081 67.8239 63.833C67.3189 64.755 66.4559 65.145 65.6789 65.145C64.1369 65.145 62.9329 63.612 65.5379 61.664C69.4549 58.733 68.0809 53.942 66.2109 53.647C66.1289 53.634 66.0479 53.628 65.9699 53.628C64.2699 53.628 63.5199 56.558 63.5199 56.558C63.5199 56.558 61.3219 62.078 57.5459 65.851C53.7699 69.625 53.5749 72.654 56.3269 76.69C58.2039 79.442 61.7969 80.273 65.4789 80.273C69.2979 80.273 73.2129 79.379 75.4069 78.81C75.5149 78.782 88.8579 75.013 87.1679 71.805C86.8839 71.266 86.4159 71.05 85.8269 71.05C83.4469 71.05 79.1179 74.592 77.2569 74.592C76.8409 74.592 76.5479 74.415 76.4279 73.983C75.6349 71.138 88.4849 69.942 87.4019 65.821C87.2109 65.092 86.6929 64.796 85.9649 64.797C82.8199 64.797 75.7639 70.328 74.2849 70.328C74.1719 70.328 74.0909 70.295 74.0469 70.225C73.3059 69.029 73.7119 68.194 78.9349 65.033C84.1579 61.871 87.8239 59.969 85.7389 57.699C85.4989 57.437 85.1589 57.321 84.7459 57.321C81.5749 57.322 74.0829 64.14 74.0829 64.14C74.0829 64.14 72.0609 66.243 70.8379 66.243C70.5569 66.243 70.3179 66.132 70.1559 65.858C69.2889 64.396 78.2089 57.636 78.7119 54.847C79.0529 52.957 78.4729 52 77.3999 52Z" fill="#FF9D0B"></path><path class="origin-bottom-left transition-transform group-hover:rotate-6" d="M56.3271 76.6898C53.5751 72.6538 53.7701 69.6248 57.5461 65.8508C61.3221 62.0778 63.5201 56.5578 63.5201 56.5578C63.5201 56.5578 64.3411 53.3518 66.2111 53.6468C68.0811 53.9418 69.4541 58.7328 65.5371 61.6638C61.6201 64.5938 66.3171 66.5848 67.8241 63.8328C69.3311 61.0808 73.4461 54.0058 75.5801 52.6528C77.7131 51.2998 79.2151 52.0578 78.7121 54.8468C78.2091 57.6358 69.2881 64.3958 70.1561 65.8588C71.0241 67.3208 74.0831 64.1398 74.0831 64.1398C74.0831 64.1398 83.6551 55.4288 85.7391 57.6988C87.8231 59.9688 84.1581 61.8708 78.9351 65.0328C73.7111 68.1938 73.3061 69.0288 74.0471 70.2248C74.7891 71.4208 86.3191 61.6998 87.4021 65.8208C88.4841 69.9418 75.6351 71.1378 76.4281 73.9828C77.2211 76.8288 85.4791 68.5978 87.1681 71.8048C88.8581 75.0128 75.5151 78.7818 75.4071 78.8098C71.0971 79.9278 60.1511 82.2968 56.3271 76.6898Z" fill="#FFD21E"></path></svg></a>
		<div class="pt-6 font-semibold text-black md:hidden md:pt-0">Website</div>

		<a class="hover:underline" href="/models">Models</a>
		<a class="hover:underline" href="/datasets">Datasets</a>
		<a class="hover:underline" href="/spaces">Spaces</a>
		<a class="hover:underline" href="/pricing">Pricing</a>
		<a class="hover:underline" href="/docs">Docs</a></nav></footer></div>

		<script>
			import("/front/build/kube-0e905ea/index.js");
			window.moonSha = "kube-0e905ea/";
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>