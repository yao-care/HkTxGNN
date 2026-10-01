---
layout: default
title: Amikacin
parent: 中證據等級 (L3-L4)
nav_order: 47
evidence_level: L4
indication_count: 10
---

# Amikacin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Amikacin：從（原適應症資料未載明）到副傷寒（Paratyphoid Fever）

## 一句話總結

Amikacin 是廣譜氨基糖苷類（aminoglycoside）抗生素，香港已有 8 張注射劑許可證，但許可證資料未載明適應症。
TxGNN 模型預測它可能對**副傷寒 (Paratyphoid Fever)** 有效，但目前**沒有臨床試驗**，只有 **10 篇文獻**，且沒有一篇提供 amikacin 治療副傷寒的療效資料。
證據等級僅 L4，建議 **Hold**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 副傷寒 (Paratyphoid Fever) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Amikacin 是廣譜氨基糖苷類抗生素，對革蘭氏陰性菌有活性，因此在試管內對副傷寒沙門氏菌（Salmonella Paratyphi）有效，在生物學上是合理的。

但這個預測在臨床上有明顯疑慮。副傷寒的病原菌主要在宿主細胞內生存，而氨基糖苷類很難進入細胞內，因此在腸熱症（enteric fever）的臨床治療上並不可靠。

檢索到的文獻主要是藥敏、流行病學監測和個案報告，沒有 amikacin 治療副傷寒的療效資料。TxGNN 分數雖高，但只反映知識圖譜的關聯，不代表臨床有效。

同一批預測中，傷寒（Typhoid Fever）有一項試管研究（PMID 19554971）顯示 amikacin 與 gentamicin 對 464 株傷寒沙門氏菌有活性。另有一項中國的小型病例系列（PMID 2598731）中，11 名患者使用 amikacin，臨床有效率僅 36.4%，ofloxacin 則為 100%。這些結果都不支持 amikacin 作為腸熱症的治療選項。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

檢索到的文獻沒有隨機對照試驗（RCT），以下為最相關的 10 篇（依類型排序）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | 世代研究 | J Indian Med Assoc | 145 名兒童的腸熱症前瞻研究，描述臨床特徵與傷寒／副傷寒的抗生素敏感性 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | 世代研究 | Pak J Biol Sci | 巴基斯坦奎達市腸熱症患者的副傷寒沙門氏菌分離與鑑定 |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | 世代研究 | Med J Armed Forces India | 45 例血液培養陽性腸熱症，評估傷寒與 A 型副傷寒菌株的藥敏，氯黴素敏感性重新出現 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | 世代研究 | JNMA | 尼泊爾教學醫院血液培養分離菌及其抗生素敏感性 |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | 世代研究 | New Microbiol | 約旦 1988–2000 年傷寒與副傷寒沙門氏菌的發生趨勢 |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | 病例系列 | J Pediatr Surg | 4 名兒童脾膿瘍以穿刺引流加抗生素成功治療 |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | 病例系列 | Mikrobiyol Bul | 48 例對傳統療法抗藥的 B 型副傷寒感染，報告抗生素治療與藥敏結果 |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | 個案報告 | Indian J Pediatr | 新生兒 A 型副傷寒敗血症，菌株對多種藥物敏感 |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | 個案報告 | Pediatr Hematol Oncol | 白血病兒童合併 B 型副傷寒無結石性膽囊炎，以 cefepime、amikacin 及 G-CSF 成功治療（多藥合併，無法歸因於 amikacin） |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | 未分類 | Indian J Pathol Microbiol | 280 株傷寒沙門氏菌中，63 株多重抗藥，但對氨基糖苷類與 ciprofloxacin 敏感（試管藥敏） |

## 香港上市資訊

香港共有 8 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34615 | ACEMYCIN INJ 250MG/ML | 未載明 | 未載明 |
| HK-35836 | SELEMYCIN INJ 500MG | 未載明 | 未載明 |
| HK-65037 | ORLOBIN INJECTION SOLUTION 1000MG/4ML | 未載明 | 未載明 |
| HK-64695 | LIKACIN AMIKACIN SOLUTION FOR INJECTION 500MG/2ML | 未載明 | 未載明 |
| HK-35832 | SELEMYCIN INJ | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻僅有藥敏、監測與個案報告，沒有 amikacin 治療副傷寒的療效資料。
- 副傷寒菌在細胞內生存，氨基糖苷類難以進入細胞內，臨床上不被視為可靠的治療選項。傷寒的小型病例系列中 amikacin 表現也遠遜於 ofloxacin。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症（目前為阻擋性缺口）
- 取得 DrugBank 作用機轉資料
- 提出細胞內滲透與藥動學的藥理學論證
- 與現行標準治療做頭對頭比較，例如針對多重抗藥菌株的替代方案

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

