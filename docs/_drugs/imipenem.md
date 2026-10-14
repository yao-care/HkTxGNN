---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 463
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

# Imipenem：從細菌性肺炎到副傷寒（Paratyphoid Fever）

## 一句話總結

Imipenem 是碳青黴烯（carbapenem）類廣譜抗生素，原本用於細菌性肺炎、腹膜炎、心內膜炎等細菌感染。
TxGNN 模型的首位預測為**瀰漫性硬皮症 (Diffuse Scleroderma)**，但該預測缺乏任何機轉或臨床證據支持，不具參考價值。
在有文獻支持的預測中，以**副傷寒 (Paratyphoid Fever)** 最合理，目前有 **5 篇文獻**（皆為間接的藥敏或監測研究）、**0 個臨床試驗**。

> 說明：以下「快速總覽」以 TxGNN 排名第一的預測（瀰漫性硬皮症）為主，並於後續章節補充其他預測的比較。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性肺炎、腹膜炎、心內膜炎、細菌性關節炎、子宮內膜炎等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 瀰漫性硬皮症 (Diffuse Scleroderma)（排名第 1） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

### 其他預測適應症比較

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 瀰漫性硬皮症 | 99.993% | L5 | Hold |
| 2 | 副傷寒 (Paratyphoid Fever) | 99.991% | L4 | 列為研究問題 |
| 3 | 沙門氏菌病 (Salmonellosis) | 99.989% | L4 | 列為研究問題 |
| 4 | 鼻竇炎 (Sinusitis) | 99.986% | L4 | Hold |
| 5 | 慢性鼻竇炎 (Chronic Rhinosinusitis) | 99.985% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Imipenem 是碳青黴烯類抗生素，透過結合青黴素結合蛋白 (PBP) 抑制細菌細胞壁合成，對多數 β-內醯胺酶（包括 ESBL）穩定，抗菌譜涵蓋革蘭氏陰性菌、革蘭氏陽性菌與厭氧菌。

**瀰漫性硬皮症（排名第 1）：** 這是一種自體免疫性纖維化疾病，沒有已知的細菌驅動因素可由碳青黴烯處理。目前找不到合理的機轉關聯，高分很可能只是知識圖譜網路鄰近性造成的假象，不建議據此推進。

**副傷寒與沙門氏菌病（排名 2、3）：** 副傷寒由副傷寒沙門氏菌引起，屬革蘭氏陰性腸內菌，在 Imipenem 抗菌譜內，對多數氟喹諾酮抗藥及 ESBL 菌株仍有體外活性。機轉上合理，但現有文獻僅為藥敏與抗藥性監測，沒有 Imipenem 的臨床療效資料。實務上碳青黴烯通常保留給廣泛抗藥 (XDR) 的傷寒型沙門氏菌。

**鼻竇炎與慢性鼻竇炎（排名 4、5）：** 細菌性鼻竇炎的常見致病菌多在抗菌譜內，但已有較窄譜的口服藥可用，靜脈注射碳青黴烯用於一般鼻竇炎不符合抗生素管理原則。慢性鼻竇炎主要為發炎與生物膜相關疾病，抗生素僅為輔助角色，機轉關聯薄弱。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下列出排名第 2 的副傷寒預測之文獻（排名第 3 至 5 的預測另有文獻，皆為間接證據，此處僅摘要說明）。

### 副傷寒（排名 2）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | 體外藥敏研究 | JPMA | 測定 ceftriaxone、azithromycin、pefloxacin、cefepime 與 imipenem 對傷寒及副傷寒沙門氏菌的最低抑菌濃度 (MIC) |
| [42621584](https://pubmed.ncbi.nlm.nih.gov/42621584/) | 2026 | 世代研究 | Cureus | 兒童傷寒與副傷寒的臨床特徵及分離菌株藥敏型態 |
| [35891850](https://pubmed.ncbi.nlm.nih.gov/35891850/) | 2022 | 橫斷面研究 | Cureus | 巴基斯坦郊區廣泛抗藥傷寒沙門氏菌的抗生素敏感性 |
| [33042671](https://pubmed.ncbi.nlm.nih.gov/33042671/) | 2020 | 世代研究 | Cureus | 伊斯蘭瑪巴德某醫院傷寒與副傷寒沙門氏菌的藥敏型態 |
| [42160545](https://pubmed.ncbi.nlm.nih.gov/42160545/) | 2026 | 世代研究 | JPMA | 兒科病人傷寒與副傷寒沙門氏菌的敏感性型態 |

### 沙門氏菌病（排名 3，精選）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32013798](https://pubmed.ncbi.nlm.nih.gov/32013798/) | 2020 | 統合分析 | Pathogens and Global Health | 伊朗沙門氏菌對氟喹諾酮抗藥盛行率 |
| [16918048](https://pubmed.ncbi.nlm.nih.gov/16918048/) | 2006 | Review | Folia Medica | 沙門氏菌病抗菌治療現況與展望 |
| [16420989](https://pubmed.ncbi.nlm.nih.gov/16420989/) | 2006 | Review | Annales de Biologie Clinique | 革蘭氏陰性菌 β-內醯胺酶與對第三代頭孢菌素、碳青黴烯的抗藥性 |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | 病例報告 | J Med Liban | 傷寒沙門氏菌感染併橫紋肌溶解與腎衰竭，以 imipenem/cilastatin 及血液透析成功治療 |

### 鼻竇炎與慢性鼻竇炎（排名 4、5）

文獻多為其他藥物（faropenem、levofloxacin、doripenem）的回顧、細菌培養與藥敏調查或病例報告，沒有 Imipenem 專屬的療效資料。

### 瀰漫性硬皮症（排名 1）

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53560 | PREPENEM FOR INJ 500MG（I & C (HONG KONG) LIMITED） | 未載明 | 未載明 |
| HK-61317 | PRIMAGAL POWDER FOR SOLUTION FOR INFUSION 500/500MG（HIND WING CO LTD） | 未載明 | 未載明 |
| HK-66808 | IMCIMILL POWDER FOR SOLUTION FOR INFUSION 500MG/500MG（CHEMILL PHARMA LIMITED） | 未載明 | 未載明 |
| HK-64660 | IMIPENEM/CILASTATIN KABI POWDER FOR SOLUTION FOR INFUSION 500MG/500MG（FRESENIUS KABI HONG KONG LIMITED） | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：癲癇、腎臟疾病、輸尿管積膿、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎。
- **藥物交互作用**：共查得 15 項。
  - **重大 (Major)**：Bupropion、Iohexol、Iopamidol
  - **中度 (Moderate)**：聚乙二醇（含電解質）、Dicoumarol、Warfarin、Lindane、Aminophylline、Dyphylline、Oxtriphylline、Theophylline、Cyclosporine、Ethinylestradiol、Mycophenolic acid、Pemetrexed
  - Bupropion 與 Lindane 等藥物與癲癇風險相關，需特別留意。

其餘警語與禁忌的詳細內容，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（瀰漫性硬皮症）；副傷寒與沙門氏菌病建議列為「研究問題」。

**理由：**
- 排名第 1 的瀰漫性硬皮症沒有任何臨床試驗或文獻，也找不到機轉關聯，應視為模型假象。
- 副傷寒與沙門氏菌病在機轉上合理，但證據僅為間接的體外藥敏與監測資料，沒有 Imipenem 的臨床療效資料。Imipenem 本身已是廣譜抗生素，這些感染也多屬其抗菌譜範圍，臨床價值取決於是否為多重抗藥菌株。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認適應症、警語與禁忌
- 補充 Imipenem 作用機轉資料
- 針對 XDR 傷寒或副傷寒沙門氏菌，蒐集 Imipenem 的臨床療效或病例系列資料
- 擬定癲癇風險與腎功能不全時的劑量調整及監測計畫，並評估抗生素管理原則下的使用條件
- 鼻竇炎類適應症除非有培養證實的抗藥感染，否則不建議推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

