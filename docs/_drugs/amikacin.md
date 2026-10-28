---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
monitor_inn: "AMIKACIN"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "meningococcemia"]
last_modified_at: 2026-10-27
description: "Amikacin：預測新適應症為副傷寒 (paratyphoid fever)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
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

## Amikacin：胺基糖苷類抗生素 → 副傷寒 (paratyphoid fever)
{: .text-alpha }

## 一句話總結

Amikacin 是一種胺基糖苷類（aminoglycoside）注射抗生素，主要用於治療革蘭氏陰性菌感染。
TxGNN 模型預測它可能對**副傷寒 (paratyphoid fever)** 有效，
但目前**沒有臨床試驗**，僅有 **8 篇文獻**，且多為流行病學、藥敏監測與個案報告，並無直接研究 Amikacin 治療副傷寒的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 副傷寒 (paratyphoid fever) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就藥物類別而言，Amikacin 屬於胺基糖苷類，一般認為其作用在於抑制細菌蛋白質合成，對多種革蘭氏陰性桿菌具抗菌活性。副傷寒由沙門氏菌（Salmonella Paratyphi）引起，同屬革蘭氏陰性腸道病原體，因此從抗菌譜來看，模型預測有一定的推論空間。

不過，這只是間接推論。腸熱症（傷寒與副傷寒）的病原菌多存在於細胞內，胺基糖苷類穿透細胞的能力有限，臨床上的標準治療多採用其他類別的抗生素。因此，體外的敏感性並不等於臨床有效。

整體而言，本預測僅屬模型推論，缺乏針對副傷寒的臨床或前臨床直接研究支持，故證據等級定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻均與副傷寒或腸熱症相關，但沒有任何一篇以 Amikacin 治療副傷寒作為直接研究對象。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | 個案報告 | Pediatric hematology and oncology | 急性淋巴性白血病孩童併發副傷寒 B 型無結石性膽囊炎，以 cefepime、amikacin 及顆粒球刺激因子合併治療後成功康復（合併用藥，無法歸因於 Amikacin） |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | 藥敏研究 | Indian J Pathol Microbiol | 280 株傷寒沙門氏菌中，部分多重抗藥株對胺基糖苷類與環丙沙星仍敏感 |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | 臨床觀察 | Mikrobiyoloji bulteni | 48 名副傷寒 B 型感染病童的抗生素治療與抗菌譜結果 |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | 藥敏研究 | Med J Armed Forces India | 北印度腸熱症菌株（含副傷寒 A 型）的藥物敏感性，氯黴素敏感性重新出現 |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | 前瞻性研究 | J Indian Med Assoc | 145 名兒童腸熱症的臨床特徵與抗生素敏感性 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | 微生物研究 | Pak J Biol Sci | 在奎達市醫院腸熱症病人中分離副傷寒沙門氏菌 |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | 流行病學 | New Microbiol | 約旦傷寒與副傷寒沙門氏菌的發生情形 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | 回顧性抗菌譜 | JNMA | 教學醫院血液培養分離菌及其藥敏模式 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34615 | ACEMYCIN INJ 250MG/ML | — | 本地資料未記錄 |
| HK-35836 | SELEMYCIN INJ 500MG | — | 本地資料未記錄 |
| HK-65037 | ORLOBIN INJECTION SOLUTION 1000MG/4ML | — | 本地資料未記錄 |
| HK-64695 | LIKACIN AMIKACIN SOLUTION FOR INJECTION 500MG/2ML | — | 本地資料未記錄 |
| HK-35832 | SELEMYCIN INJ | — | 本地資料未記錄 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共 100 筆交互作用紀錄，其中列為嚴重（Major）的包括：
  - 硫酸鎂（Magnesium sulfate）
  - 甘露醇（Mannitol）

  列為中度（Moderate）的包括 Amphotericin B（含各種劑型）、Kanamycin、Neomycin、阿斯匹靈，以及多種氫離子幫浦抑制劑（如 omeprazole、esomeprazole、lansoprazole、pantoprazole、rabeprazole）等。

- **需特別留意的疾病背景**：本報告彙整的資料顯示，下列疾病族群需謹慎評估：腎臟疾病、重症肌無力與神經肌肉接合部疾病、帕金森氏症或類帕金森症候群、高血鈣與磷代謝異常、腎鈣質沉著症、中樞神經性眩暈。這些並非仿單禁忌症文字，使用前仍須對照原廠仿單確認。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（0.9982），但沒有任何臨床試驗，文獻也沒有直接評估 Amikacin 治療副傷寒的研究，故證據等級為 L5。
- 胺基糖苷類對細胞內寄生的沙門氏菌穿透力有限，且已有其他類別抗生素作為標準治療，Amikacin 的臨床定位不明確。

**若要推進需要：**
- 補充作用機轉資料及針對副傷寒的體外與動物模型研究
- 與現行標準治療的比較性療效資料
- 取得香港核准仿單，確認警語、禁忌症與腎毒性、耳毒性的監測要求
- 評估腎功能不全與神經肌肉疾病族群的風險管理計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

