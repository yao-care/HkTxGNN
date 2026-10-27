---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amikacin：預測新適應症為副傷寒 (Paratyphoid Fever)（證據等級 L5）。原適應症：細菌性肺炎、綠膿桿菌感染、膽管炎、細菌性腦膜炎、大腸桿菌感染等"
monitor_inn: "AMIKACIN"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "meningococcemia"]
---

# Amikacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Amikacin：從細菌感染到副傷寒
{: .text-alpha }

## 一句話總結

Amikacin 是一種胺基糖苷類（aminoglycoside）抗生素，原本用於治療細菌性肺炎、綠膿桿菌感染、細菌性腦膜炎等革蘭氏陰性菌感染。
TxGNN 模型預測它可能對**副傷寒 (Paratyphoid Fever)** 有效，但目前**沒有臨床試驗**，只有 **8 篇文獻**，且多為流行病學與抗生素敏感性調查，缺乏直接的療效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性肺炎、綠膿桿菌感染、膽管炎、細菌性腦膜炎、大腸桿菌感染等（香港許可證未載明適應症文字，以模型知識圖譜的適應症為準） |
| 預測新適應症 | 副傷寒 (Paratyphoid Fever) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Amikacin 是胺基糖苷類抗生素，一般認為其作用是抑制細菌蛋白質合成，對多種革蘭氏陰性菌有活性。副傷寒由沙門氏菌 (Salmonella Paratyphi) 引起，屬於革蘭氏陰性菌感染，與 Amikacin 原有的適應症在病原類型上相近，這是模型給出高分的可能原因。

不過，沙門氏菌是細胞內感染，胺基糖苷類穿透細胞的能力有限。標準治療通常使用氟喹諾酮類、azithromycin 或第三代頭孢菌素。因此，這個預測在機轉上只有間接支持。

另外，同一預測清單中的傷寒 (Typhoid Fever) 有一篇體外研究（PMID 19554971）顯示 Amikacin 對傷寒沙門氏菌具抗菌活性。副傷寒與傷寒同屬腸熱病，這項研究可作為旁證，但仍不等於臨床療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下列文獻多數尚未完成研究類型分類，內容以流行病學、抗生素敏感性調查與個案報告為主。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatric Hematology and Oncology | 一名急性淋巴芽細胞白血病男童因副傷寒 B 菌引起無結石性膽囊炎，以 cefepime、amikacin 及顆粒球刺激因子合併治療後成功痊癒（複方治療，無法單獨歸因於 Amikacin） |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | 臨床報告 | Mikrobiyoloji Bulteni | 報告 48 名對傳統治療有抗藥性的副傷寒 B 感染患者的抗生素治療與藥敏結果 |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | 藥敏調查 | Medical Journal, Armed Forces India | 印度北部腸熱病菌株（含副傷寒 A）的體外藥敏，重點為 chloramphenicol 敏感性重現 |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | 前瞻性觀察研究 | Journal of the Indian Medical Association | 145 名兒童腸熱病的臨床特徵與抗生素敏感性 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | 微生物學研究 | Pakistan Journal of Biological Sciences | 巴基斯坦奎達地區副傷寒沙門氏菌的分離與鑑定 |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | 流行病學 | The New Microbiologica | 約旦傷寒與副傷寒沙門氏菌的發生率 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | 抗生素敏感性回顧 | JNMA | 教學醫院血液培養分離株及其抗生素敏感性 |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case series | Journal of Pediatric Surgery | 4 名兒童脾膿瘍以穿刺引流合併抗生素治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34615 | ACEMYCIN INJ 250MG/ML | 注射劑 | 未提供 |
| HK-35836 | SELEMYCIN INJ 500MG | 注射劑 | 未提供 |
| HK-65037 | ORLOBIN INJECTION SOLUTION 1000MG/4ML | 注射劑 | 未提供 |
| HK-64695 | LIKACIN AMIKACIN SOLUTION FOR INJECTION 500MG/2ML | 注射劑 | 未提供 |
| HK-35832 | SELEMYCIN INJ | 注射劑 | 未提供 |

目前共 8 張有效許可證，皆為單方注射製劑，無已註銷者。以上僅列出 5 張主要許可證。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、輸尿管積膿、高血鈣、腎鈣質沉著症、磷代謝疾病、中樞神經性眩暈、重症肌無力（含成人型）、神經肌肉接合部疾病、帕金森氏症與類帕金森症。此資料來自知識圖譜的藥物與疾病關聯，並非仿單文字。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重 (Major)：Magnesium sulfate、Mannitol
  - 中度 (Moderate)：Amphotericin B（含各種劑型）、Kanamycin、Neomycin、Acetylsalicylic acid、Mesalazine 及多種氫離子幫浦抑制劑（如 Omeprazole、Pantoprazole、Esomeprazole）

仿單的警語與禁忌資料目前缺漏，使用前請參考原廠仿單。胺基糖苷類一般需留意腎毒性與耳毒性。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何臨床試驗，文獻多為流行病學與藥敏調查，僅有一例複方治療的個案報告，沒有 Amikacin 用於副傷寒的直接療效證據，因此證據等級為 L5。
- 沙門氏菌為細胞內感染，胺基糖苷類穿透性差，且現有標準治療選擇充足，Amikacin 的臨床定位不明確。

**若要推進需要：**
- 取得 Amikacin 對副傷寒沙門氏菌的體外藥敏與動物模型數據
- 補充 Amikacin 的作用機轉資料與香港仿單的警語、禁忌資料
- 與現行標準治療（氟喹諾酮類、azithromycin、頭孢菌素）比較的臨床研究設計
- 針對多重抗藥菌株（如對一線藥物抗藥者）評估是否有救援治療的價值
- 腎毒性與耳毒性的監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

