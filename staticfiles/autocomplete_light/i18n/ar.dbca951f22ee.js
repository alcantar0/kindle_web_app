/*! Select2 4.1.0-rc.0 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(n){var e;(e=n&&n.fn&&n.fn.select2&&n.fn.select2.amd?n.fn.select2.amd:e).define("select2/i18n/ar",[],function(){return{errorLoading:function(){return"لا يمكن تحميل النتائج"},inputTooLong:function(n){return"الرجاء حذف "+(n.input.length-n.maximum)+" عناصر"},inputTooShort:function(n){return"الرجاء إضافة "+(n.minimum-n.input.length)+" عناصر"},loadingMore:function(){return"جاري تحميل نتائج إضافية..."},maximumSelected:function(n){return"تستطيع إختيار "+n.maximum+" بنود فقط"},noResults:function(){return"لم يتم العثور على أي نتائج"},searching:function(){return"جاري البحث…"},removeAllItems:function(){return"قم بإزالة كل العناصر"}}}),e.define,e.require},event=new CustomEvent("dal-language-loaded",{lang:"ar"});document.dispatchEvent(event);