---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 5
---

# Imipenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imipenem：從廣效抗菌治療到多重抗藥性沙門氏菌感染（副傷寒熱與沙門氏菌症）

## 一句話總結

Imipenem 是廣效碳青黴烯類（carbapenem）抗生素，透過抑制細菌細胞壁合成產生殺菌作用。
TxGNN 模型針對此藥共預測出 5 個候選新適應症，其中**副傷寒熱 (Paratyphoid Fever)** 與**沙門氏菌症 (Salmonellosis)** 有實際文獻支持（分別 4 篇與 20 篇），指向 imipenem 可作為多重抗藥性 (MDR/XDR) 腸桿菌科感染的替代治療選項；其餘候選（鼻竇炎、慢性鼻竇炎、瀰漫性硬皮症）證據薄弱或不具機轉合理性，建議保留或排除。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效抗菌感染治療（碳青黴烯類抗生素）— 香港未上市，無許可證資料可查原核准適應症 |
| 主要預測新適應症 | 副傷寒熱 (Paratyphoid Fever)、沙門氏菌症 (Salmonellosis) |
| TxGNN 預測分數 | 副傷寒熱 99.99%（rank 406）／沙門氏菌症 99.99%（rank 450） |
| 證據等級 | L3（觀察性研究、體外藥敏及個案報告，無 RCT） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails（限縮於 MDR/XDR 感染族群） |

> ⚠️ 本次評估共產生 5 個候選新適應症，證據強度差異極大，詳見下表。

---

## 候選適應症總覽

| 排名 | 候選適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | 瀰漫性硬皮症 (Diffuse Scleroderma) | 99.99% | L5 | S0 | **Hold（建議排除）** |
| 2 | 副傷寒熱 (Paratyphoid Fever) | 99.99% | L3 | S2 | Proceed with Guardrails |
| 3 | 沙門氏菌症 (Salmonellosis) | 99.99% | L3 | S2 | Proceed with Guardrails |
| 4 | 鼻竇炎 (Sinusitis) | 99.99% | L4 | S1 | Research Question |
| 5 | 慢性鼻竇炎 (Chronic Rhinosinusitis) | 99.98% | L4 | S0 | Hold |

**觀察重點：** 五個候選的 TxGNN 分數皆落在 99.98%–99.99% 區間，彼此幾乎無法區分，顯示分數本身對候選排序的鑑別力有限，必須以下游證據（臨床試驗/文獻/機轉）作為主要判斷依據。這也印證了排名第 1 的「瀰漫性硬皮症」雖分數最高，卻是缺乏任何實證與機轉支持的偽陽性預測。

---

## 為什麼這些預測合理？

目前缺乏 Imipenem 完整的 DrugBank MOA 描述（資料缺口 DG002），但根據相關文獻中反覆提及的藥理背景，Imipenem 屬於碳青黴烯類 β-內醯胺抗生素，透過與細菌青黴素結合蛋白 (PBP) 結合，抑制細胞壁肽聚醣合成而產生殺菌效果，對包含腸桿菌科 (Enterobacteriaceae) 在內的革蘭氏陰性菌具廣效活性。

**副傷寒熱與沙門氏菌症**：Salmonella Typhi/Paratyphi 及其他 Salmonella spp. 皆屬腸桿菌科，對 imipenem 具內生敏感性。文獻顯示，在喹諾酮抗藥或廣泛抗藥 (XDR) 傷寒沙門氏菌流行地區（如巴基斯坦、印度次大陸），carbapenem 類已被列為經驗性/挽救性治療選項，並有新生兒腦膜炎個案報告佐證其臨床可行性。這並非全新機轉假說，而是現有國際治療指引中對 MDR/XDR 腸道熱病既有的 salvage therapy 延伸。

**鼻竇炎／慢性鼻竇炎**：一般社區型鼻竇炎致病菌（如 S. pneumoniae、H. influenzae）並不需要碳青黴烯類藥物，相關文獻多為罕見院內病原（Flavimonas oryzihabitans、Nocardia nova）造成之個案，或與 imipenem 無直接關聯的其他藥物回顧文獻，機轉關聯薄弱。

**瀰漫性硬皮症**：屬自體免疫介導的纖維化疾病，病理核心為異常膠原沉積與血管病變，與 imipenem 的細菌細胞壁合成抑制機轉無任何已知交集，判斷為知識圖譜嵌入產生的偽陽性關聯。

---

## 各候選適應症詳細證據

### 1. 副傷寒熱 (Paratyphoid Fever) — L3 / Proceed with Guardrails

**臨床試驗**：目前無相關臨床試驗登記

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | 體外藥敏 | JPMA | 測定 ceftriaxone、azithromycin、pefloxacin、cefepime 與 imipenem 對 S. Typhi/Paratyphi 之最小抑菌濃度 (MIC) |
| [35891850](https://pubmed.ncbi.nlm.nih.gov/35891850/) | 2022 | 回顧 | Cureus | 巴基斯坦 XDR 傷寒沙門氏菌對現有抗生素之敏感性評估，涉及 carbapenem 類替代選項 |
| [33042671](https://pubmed.ncbi.nlm.nih.gov/33042671/) | 2020 | 世代／監測 | Cureus | 伊斯蘭馬巴德三級醫院 S. Typhi/Paratyphi 抗生素敏感模式回溯性分析 |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | 個案報告 | The Journal of Infection | 新生兒喹諾酮抗藥 S. paratyphi B 腦膜炎個案，佐證 carbapenem 類臨床可行性 |

### 2. 沙門氏菌症 (Salmonellosis) — L3 / Proceed with Guardrails

**臨床試驗**：目前無相關臨床試驗登記

**文獻證據**（20 篇中列出證據等級最高之 10 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32013798](https://pubmed.ncbi.nlm.nih.gov/32013798/) | 2020 | 統合分析 | Pathogens and Global Health | 伊朗氟喹諾酮抗藥 Salmonella 血清型盛行率統合分析 |
| [38984026](https://pubmed.ncbi.nlm.nih.gov/38984026/) | 2024 | 世代／監測 | Translational Pediatrics | 中國郴州兒童食源性沙門氏菌症血清型與抗藥性分析 |
| [3469191](https://pubmed.ncbi.nlm.nih.gov/3469191/) | 1986 | 臨床評估 | J Antimicrob Chemother | Imipenem/cilastatin 用於院內感染與多重抗藥病原之早期臨床評估 |
| [41277208](https://pubmed.ncbi.nlm.nih.gov/41277208/) | 2025 | 世代／監測 | J Assoc Physicians India | 印度三級醫院非傷寒沙門氏菌感染盛行率與抗藥性分析 |
| [2945941](https://pubmed.ncbi.nlm.nih.gov/2945941/) | 1986 | 兒科臨床評估 | 日本抗生物質醫學雜誌 | Imipenem/cilastatin 用於 8 名兒童感染（含沙門氏菌）之基礎與臨床評估 |
| [12917244](https://pubmed.ncbi.nlm.nih.gov/12917244/) | 2003 | 體外藥敏 | J Antimicrob Chemother | Faropenem 與 imipenem 對 ciprofloxacin 抗藥菌株之活性比較 |
| [14659660](https://pubmed.ncbi.nlm.nih.gov/14659660/) | 2003 | 體外藥敏 | Int J Antimicrob Agents | Ceftazidime、imipenem、pefloxacin 併用對 S. typhimurium 等病原之協同效果 |
| [9559775](https://pubmed.ncbi.nlm.nih.gov/9559775/) | 1998 | 機轉研究 | Antimicrob Agents Chemother | Imipenem 與 ceftazidime 誘導 S. typhi 內毒素 (LPS) 釋放之動力學差異 |
| [33248418](https://pubmed.ncbi.nlm.nih.gov/33248418/) | 2021 | 分子鑑定 | Diagn Microbiol Infect Dis | 四川 imipenem 不敏感 S. Typhimurium 之新型第一類整合子與轉位子鑑定 |
| [36278497](https://pubmed.ncbi.nlm.nih.gov/36278497/) | 2023 | 回顧 | Z Naturforsch C | 新型氟喹諾酮類化合物對食源性致病菌（含 Salmonella）之抗菌活性 |

### 3. 鼻竇炎 (Sinusitis) — L4 / Research Question

**臨床試驗**：目前無相關臨床試驗登記

**文獻證據**（僅列與 imipenem／鼻竇感染直接相關者）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16200963](https://pubmed.ncbi.nlm.nih.gov/16200963/) | 2005 | 細菌學調查 | 中華耳鼻咽喉頭頸外科雜誌 | 慢性鼻竇炎病患致病菌分布與抗藥性調查 |
| [12953957](https://pubmed.ncbi.nlm.nih.gov/12953957/) | 2003 | 個案報告 | Scand J Infect Dis | 罕見病原 Flavimonas oryzihabitans 引起之菌血症合併鼻竇炎 |
| [26471040](https://pubmed.ncbi.nlm.nih.gov/26471040/) | 2016 | 個案報告 | Eur Ann Otorhinolaryngol | Nocardia nova 蝶竇炎合併顳下窩膿瘍 |
| [38617893](https://pubmed.ncbi.nlm.nih.gov/38617893/) | 2024 | 世代研究 | Curr Ther Res | 惡性腫瘤患兒副鼻竇感染之微生物與分子研究 |

> 此類文獻多為罕見或院內病原個案，非一般鼻竇炎之標準實證，僅適用於高度抗藥或免疫低下族群的特殊感染情境，需嚴格限縮族群並考量抗生素管理 (stewardship) 風險。

### 4. 慢性鼻竇炎 (Chronic Rhinosinusitis) — L4 / Hold

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37042371](https://pubmed.ncbi.nlm.nih.gov/37042371/) | 2022 | 細菌學調查 | Kathmandu Univ Med J | 慢性鼻竇炎門診病患細菌相與抗生素敏感模式 |
| [27192905](https://pubmed.ncbi.nlm.nih.gov/27192905/) | 2016 | 細菌學調查 | 臨床耳鼻咽喉頭頸外科雜誌 | 合併/未合併鼻息肉之慢性鼻竇炎病患細菌分布與藥敏 |
| [40697614](https://pubmed.ncbi.nlm.nih.gov/40697614/) | 2025 | 世代研究 | World J Diabetes | 糖尿病合併慢性鼻竇炎患者鼻分泌物培養與術後復發因子 |
| [34844745](https://pubmed.ncbi.nlm.nih.gov/34844745/) | 2022 | 體外實驗 | Pathology | 奈米銀與抗生素併用對抗藥性生物膜（含 MRSA）之效果 |

> 無任何文獻顯示 imipenem 對慢性鼻竇炎具直接療效，且無資料顯示其優於現行標準治療（如 amoxicillin-clavulanate、鼻用類固醇），**建議 Hold，不進入後續研究排程**。

### 5. 瀰漫性硬皮症 (Diffuse Scleroderma) — L5 / Hold（建議排除）

無任何臨床試驗或文獻支持。此為自體免疫纖維化疾病，與 imipenem 之抗菌機轉無合理關聯，極可能為 TxGNN 知識圖譜嵌入產生的偽陽性關聯，**建議直接排除，不進入後續研究排程**。

---

## 香港上市資訊

目前 Imipenem 在香港**未上市**，無有效許可證（total_licenses = 0），因此無法取得原核准適應症、劑型或仿單資訊作為比對基礎。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 重要缺口：本次評估的資料缺口清單標記「TFDA/仿單警語與禁忌」為 **Blocking** 等級（DG001），代表在取得完整安全性仿單資料前，無法完成 S1 安全性初評。即便部分候選適應症（副傷寒熱、沙門氏菌症）的證據面已達 S2 階段，此安全性資料缺口仍是全案推進前必須解決的前提。

---

## 結論與下一步

**決策：Proceed with Guardrails（限於副傷寒熱／沙門氏菌症兩項候選，其餘三項 Hold）**

**理由：**
- 副傷寒熱與沙門氏菌症皆有多篇體外藥敏、世代監測及個案研究支持 imipenem 對 MDR/XDR 腸桿菌科病原的殺菌活性，且機轉合理、非全新假說，可視為現有 salvage therapy 的實證延伸。
- 鼻竇炎相關文獻皆為罕見病原個案，機轉關聯薄弱，僅列為研究假說；慢性鼻竇炎與瀰漫性硬皮症則缺乏機轉合理性或直接證據，建議排除或暫緩。

**若要推進需要：**
- 補齊 Imipenem 完整仿單警語、禁忌症與 DDI 資料（DG001，Blocking，需優先解決）
- 補齊 DrugBank 作用機轉 (MOA) 完整描述（DG002）
- 針對副傷寒熱／沙門氏菌症，限縮於 MDR/XDR 確診族群，設計具對照組之前瞻性研究以補足 L3 證據等級不足處
- 若考慮於香港申請適應症擴增，須先確認 imipenem 於當地上市與許可證狀態（目前為 0 張許可證，屬阻斷性缺口）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

