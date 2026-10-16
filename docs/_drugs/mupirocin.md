---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 602
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mupirocin：預測新適應症為葡萄球菌燙傷樣皮膚症候群（證據等級 L5）。原適應症：膿痂疹、大泡性膿痂疹"
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis", "neurotrophic keratopathy", "cutaneous candidiasis", "vaginal discharge", "exposure keratitis", "leukoplakia of vagina", "non-human animal disease", "staphylococcal scalded skin syndrome", "bacterial vaginosis"]
---

# Mupirocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Mupirocin：從膿痂疹到葡萄球菌燙傷樣皮膚症候群

## 一句話總結

Mupirocin 是外用抗生素，原本用於膿痂疹（impetigo）及大泡性膿痂疹的治療。
TxGNN 模型的首位預測為「膿胸」，但該預測缺乏任何證據且機轉上不合理。
本報告改以證據最完整的**葡萄球菌燙傷樣皮膚症候群 (Staphylococcal Scalded Skin Syndrome, SSSS)** 為主要評估對象：目前有 **0 個臨床試驗**，但有 **13 篇文獻**（以觀察性研究、病例報告與回顧為主）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 膿痂疹、大泡性膿痂疹 |
| 預測新適應症 | 葡萄球菌燙傷樣皮膚症候群（SSSS，TxGNN 排名第 9；排名第 1 的膿胸缺乏證據且機轉不合理，故改評估 SSSS） |
| TxGNN 預測分數 | 95.57%（SSSS）；排名第 1 的膿胸為 99.49% |
| 證據等級 | L3（SSSS：觀察性研究與回顧，無 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張（皆為有效的單一成分許可證） |
| 建議決策 | Proceed with Guardrails（僅限 SSSS，作為輔助治療） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未提供）。根據已知資訊，mupirocin 可抑制細菌的異白胺酸 tRNA 合成酶，對金黃色葡萄球菌有活性。

SSSS 由會產生表皮剝脫毒素的金黃色葡萄球菌引起，與大泡性膿痂疹是同一種病原體所致、病程上相連的疾病譜系。大泡性膿痂疹是 mupirocin 的既有適應症，因此局部使用 mupirocin 作為輔助治療與去除細菌定植，在機轉上合理。

需要強調：mupirocin 只能作為**輔助**，不能取代全身性抗葡萄球菌抗生素。

**其他預測的評估：**
- **膿胸、陰道分泌物、陰道白斑、細菌性陰道病：** 僅有模型預測或間接證據。mupirocin 為外用製劑，無有意義的全身或胸腔暴露，且對厭氧菌活性有限，機轉關聯弱。
- **點狀上皮角膜結膜炎、神經營養性角膜病變、暴露性角膜炎：** 病因多為病毒、發炎或神經性問題。軟膏並非眼用設計，且 1993 年體外研究顯示對角膜上皮有毒性疑慮。
- **皮膚念珠菌症：** 僅有 1991 年一篇報告（標題顯示研究設計無法確認）與一篇病例報告，證據間接。mupirocin 本身抗黴菌活性很弱。
- **非人類動物疾病：** 為本體論的非特異分類，不屬可行動的適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

以下為 SSSS 的主要文獻（依證據價值挑選）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | 回溯性世代研究 | Clin Cosmet Investig Dermatol | 比較不同靜脈抗生素合併 2% mupirocin 軟膏治療兒童 SSSS 的療程、影響因素與費用 |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Rev Anti Infect Ther | 嬰兒大泡性膿痂疹與 SSSS 的治療回顧 |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | 回顧 | Dermatol Clin | 控制葡萄球菌在皮膚疾病處置的重要性；外用 mupirocin 對膿痂疹等是重要新增選項 |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | 病例系列 | Adv Neonatal Care | 新生兒 SSSS 的辨識與傷口照護 |
| [42509990](https://pubmed.ncbi.nlm.nih.gov/42509990/) | 2026 | 回溯性世代研究 | Children (Basel) | 三級兒童醫院 11 年 SSSS 的流行病學、微生物與處置 |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | 流行病學/世代 | Pediatr Infect Dis J | 德州休士頓 ST121 菌株引起的 SSSS 病例增加 |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | 流行病學/分子研究 | J Med Microbiol | 新興的 ST121 clone 具 mupirocin 與 fusidic acid 抗藥性 |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | 回溯性研究 | J Clin Microbiol | 對 mupirocin 與 fusidic acid 抗藥的菌株，主要引起皮膚感染 |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | 群聚調查 | J Hosp Infect | 新生兒 SSSS 院內群聚的調查與控制 |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | 分子流行病學 | Pediatr Infect Dis J | 早產兒 SSSS 的分子流行病學與感染控制 |

**其他預測的零星文獻：** 皮膚念珠菌症有 [PMID 1678836](https://pubmed.ncbi.nlm.nih.gov/1678836/)（1991，Lancet，mupirocin 用於皮膚念珠菌症，設計未確認）；細菌性陰道病有 [PMID 1815427](https://pubmed.ncbi.nlm.nih.gov/1815427/)（1991，一例 MRSA 陰道炎以 mupirocin 清除，並非細菌性陰道病）；暴露性角膜炎有 [PMID 8222720](https://pubmed.ncbi.nlm.nih.gov/8222720/)（1993，體外研究，提示角膜上皮毒性）。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-28186 | BACTROBAN OINT 2%（GlaxoSmithKline） | 軟膏 | 資料未提供 |
| HK-33588 | BACTROBAN NASAL OINT 2%（GlaxoSmithKline） | 鼻用軟膏 | 資料未提供 |
| HK-55473 | AROCIN OINTMENT 2%（Bright Future） | 軟膏 | 資料未提供 |
| HK-55952 | MUPRIN OINTMENT 2%（Taisho） | 軟膏 | 資料未提供 |
| HK-65498 | BACTEROCIN OINTMENT 2% W/W（Meyer BPC） | 軟膏 | 資料未提供 |

另有 9 張有效許可證，皆為 2% 軟膏類單一成分產品。

---

## 安全性考量

- **知識圖譜中的禁忌疾病：** 皮膚炎（dermatitis；來自知識圖譜關聯，並非仿單內容）。
- **藥物交互作用：** 共查得 100 筆，但皆未標示嚴重程度（等級未知），例如 calcitriol、clotrimazole、morphine、metformin、vancomycin 等。外用製劑的臨床意義需另行評估。
- **使用於 SSSS 的注意事項：** 新生兒皮膚剝脫處可能增加吸收（聚乙二醇基質）；需注意抗藥性（文獻已報告 mupirocin 抗藥菌株）；應限制療程。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（僅限 SSSS；其餘預測適應症皆為 Hold）**

**理由：**
- SSSS 與既有適應症（大泡性膿痂疹）病原體相同，且有一項 2023 年研究以 mupirocin 作為輔助治療，但證據僅為觀察性，無 RCT 與已登記試驗，只能定位為全身性抗生素的輔助。
- 其他預測多為純模型預測、機轉不合理，或有安全疑慮（如眼部使用），應暫緩。皮膚念珠菌症可列為研究問題，但證據不足。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症（目前為阻擋性資料缺口）
- 補充詳細作用機轉資料
- 設計 SSSS 輔助治療的前瞻性或對照研究，並納入新生兒的吸收與安全性監測
- 評估本地 mupirocin 抗藥性流行情形
- 確認各許可證的劑型與核准適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

