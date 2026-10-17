---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Arsenic Trioxide：預測新適應症為骨髓發育不良症候群 (Myelodysplastic Syndrome)（證據等級 L5）。原適應症：急性前骨髓性白血病、骨髓單核球白血病、急性骨髓性白血病（伴 inv(16) 或 t(16"
monitor_inn: "ARSENIC TRIOXIDE"
predicted_indications: ["unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts", "aregenerative anemia", "partial deletion of the long arm of chromosome 5", "myelodysplastic syndrome", "Ewing sarcoma", "dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
---

# Arsenic Trioxide
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

# 三氧化二砷（Arsenic Trioxide）：從急性前骨髓性白血病到骨髓發育不良症候群

## 一句話總結

三氧化二砷原本用於治療急性前骨髓性白血病（APL）及相關骨髓性白血病。
TxGNN 模型預測分數最高的新適應症為**未分類骨髓發育不良症候群**，但該項目本身沒有任何直接證據。
證據最充分的是同屬 MDS 範疇的**骨髓發育不良症候群 (Myelodysplastic Syndrome)**，目前有 **19 個臨床試驗**和 **20 篇文獻**（含 1 篇系統性回顧與網絡統合分析）支持這個方向。

> 說明：預測分數排名第一的疾病（未分類 MDS）沒有直接的試驗或文獻，因此下方臨床試驗與文獻證據以證據最完整的「骨髓發育不良症候群」為主。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性前骨髓性白血病、骨髓單核球白血病、急性骨髓性白血病（伴 inv(16) 或 t(16;16)） |
| 預測新適應症 | 骨髓發育不良症候群 (Myelodysplastic Syndrome)（證據最完整者）；分數最高者為未分類骨髓發育不良症候群 |
| TxGNN 預測分數 | 99.91%（骨髓發育不良症候群）；99.93%（未分類 MDS，無直接證據） |
| 證據等級 | L2（骨髓發育不良症候群）；未分類 MDS 為 L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（整體）；MDS 方向可列為 Research Question，若推進需採 Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位無資料）。不過根據文獻，三氧化二砷具有促凋亡、抗增殖與誘導分化作用，並能調控 NF-κB/FLIP 與 BCL2 家族基因，也可能重新活化 TP53 功能。這些機轉在 APL 以外的骨髓性惡性疾病中同樣可能發揮作用。

原適應症 APL 與 MDS 同屬骨髓性造血系統疾病，MDS 有部分病人會轉化為急性骨髓性白血病。因此 TxGNN 給出的高分，主要反映 MDS 類疾病之間的相似性。

需特別提醒：排名第一至第三、第五的項目（未分類 MDS、先天性鐵粒幼細胞貧血、del(5q) 等）以及肉瘤類項目（皮膚纖維肉瘤、脂肪肉瘤、卵巢黏液樣脂肪肉瘤）皆無任何直接證據，分數很可能只是圖譜相似性的結果。Ewing 肉瘤僅有前臨床證據。

## 臨床試驗證據

以下為「骨髓發育不良症候群」相關試驗（列出最相關 10 個，依相關性分級排序）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00093366](https://clinicaltrials.gov/study/NCT00093366) | Phase 1/2 | 完成 | 32 | 三氧化二砷併用 etanercept 治療晚期 MDS，為最直接相關的已完成 MDS 研究 |
| [NCT00195104](https://clinicaltrials.gov/study/NCT00195104) | Phase 1/2 | 完成 | 87 | 三氧化二砷併用低劑量 ara-C 治療高風險 MDS 與預後不良 AML |
| [NCT00251511](https://clinicaltrials.gov/study/NCT00251511) | Phase 2 | 終止 | 60 | 三氧化二砷併用 thalidomide 治療各風險等級 MDS |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | 完成 | 92 | 隨機比較 decitabine、decitabine＋carboplatin、decitabine＋砷於復發/難治/老年 AML 與 MDS |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | 完成 | 30 | 三氧化二砷併用 gemtuzumab ozogamicin 治療晚期 MDS |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | 完成 | 7 | decitabine＋三氧化二砷＋維生素 C 的先導試驗，主要評估安全性 |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | 完成 | 13 | 靜脈 decitabine 併用三氧化二砷與維生素 C，提供組合安全性資料 |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | 招募中 | 30 | 口服三氧化二砷（Arsenol）併用維生素 C 與低強度治療，用於 TP53 突變髓系惡性腫瘤 |
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | 招募中 | 24 | 口服砷用於 ESA 與 luspatercept 失敗的低風險 MDS，劑量遞增與擴展 |
| [NCT07737769](https://clinicaltrials.gov/study/NCT07737769) | Phase 1 | 尚未招募 | 20 | 異體移植 AML/MDS 中以三氧化二砷重新活化 TP53、預防復發 |

另有多項試驗被提前終止且樣本極小（如 NCT00104806 僅 5 人、NCT00234000 與 NCT00118196 各 1 人），以及一項 Phase 3 試驗 NCT03377725（decitabine＋砷 vs. decitabine）已撤回，未收案。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | 系統性回顧與網絡統合分析 | Hematology | 評估含三氧化二砷方案於 MDS 的療效與不良事件，並探討最佳組合；既有試驗樣本小且結論不一 |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase I/II 臨床研究 | Leukemia Research | 三氧化二砷併用低劑量 cytarabine，49 位中高/高風險 MDS，17% 達完全緩解，4 週內死亡率 8% |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | 臨床研究 | Leukemia Research | 砷、thalidomide 與 retinoic acid 併用於較高風險 MDS 的療效與安全性 |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Curr Hematol Malig Rep | 三氧化二砷具促凋亡、抗增殖、抗血管新生作用，單用或併用於 MDS |
| [15610661](https://pubmed.ncbi.nlm.nih.gov/15610661/) | 2005 | Review | Curr Hematol Rep | 同上作者的 MDS 治療回顧 |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Review | Clin Lymphoma Myeloma | 砷於白血病與 MDS 的新數據；APL 復發病人緩解率超過 80% |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | 前臨床 | Immunopharmacol Immunotoxicol | 比較雄黃與三氧化二砷在 MDS 小鼠模型的免疫變化 |
| [41398777](https://pubmed.ncbi.nlm.nih.gov/41398777/) | 2025 | 前臨床 | Medicine | 雷公藤甲素併用砷經抑制 NF-κB 誘導 MDS 細胞凋亡 |
| [27665715](https://pubmed.ncbi.nlm.nih.gov/27665715/) | 2016 | 前臨床 | Mol Med Rep | 砷與雷公藤甲素於 SKM-1 MDS 細胞株協同誘導凋亡 |
| [12886236](https://pubmed.ncbi.nlm.nih.gov/12886236/) | 2003 | 綜述 | Leukemia | 討論 Trisenox 在 MDS 治療的機會 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59724 | ARSENOL ORAL SOLUTION 1MG/ML | 口服溶液 | 目前無可用的核准適應症資料 |

製造商為 UNICORN LABORATORIES O/B AMERICAN UNICORN LABORATORIES LIMITED，狀態為有效（單一成分）。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗腫瘤藥物（砷製劑，具促凋亡與誘導分化作用） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 心電圖（QTc）、電解質（鉀、鎂）、血液學參數（CBC）、肝腎功能 |
| 處置防護 | 請參考原廠仿單的處置規範 |

請參考原廠仿單的警語與注意事項。上述監測項目是依據下列安全性資料中的心臟與電解質相關風險所列。

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**：長 QT 症候群（含家族性）、尖端扭轉型心律不整、房室傳導阻滯、鉀缺乏、腎臟疾病、肝臟疾病、膽囊疾病、輸尿管積膿。
- **藥物交互作用**：共查得 100 筆，以下為部分重要者。
  - 嚴重（Major）：Hydrocortisone、Amphotericin B（含脂質複合體、膽固醇硫酸鹽、脂質體劑型）、Cisapride、Clarithromycin、Dolasetron、Granisetron、Levofloxacin。多數與 QT 延長或電解質失衡風險有關。
  - 中度（Moderate）：Famotidine、Loperamide、Bisacodyl、Castor oil、Glycerin、Lactitol、Lactulose、Magnesium citrate、Magnesium hydroxide（多為瀉劑類，可能造成電解質流失）。
  - 輕微（Minor）：Metronidazole。

香港仿單的警語與禁忌尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold（整體）；MDS 方向可列為研究問題（Research Question），若推進須採 Proceed with Guardrails**

**理由：**
- 預測分數最高的前幾項（未分類 MDS、先天性鐵粒幼細胞貧血、del(5q)）及多數肉瘤類項目沒有直接證據，僅為 L5 模型預測。
- MDS 一般項目有多個 Phase 1/2 試驗與一篇系統性回顧，但多數試驗規模小或提前終止、反應有限，且沒有已完成的 Phase 3 驗證，因此證據等級為 L2。
- 安全性方面有 QT 延長與電解質相關的重大風險，用藥須嚴格控管。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌，並補充 MOA 資料。
- 針對 MDS 設計以 TP53 突變或低風險 MDS 為焦點的隨機對照試驗（可參考進行中的 NCT06778187、NCT06670222）。
- 建立心電圖（QTc）、鉀鎂電解質與藥物交互作用的監測計畫，避免併用 QT 延長藥物。
- 確認口服劑型 Arsenol 在香港的核准適應症與用途範圍。
- 對再生不良性貧血、Ewing 肉瘤等僅有小型研究或前臨床證據的方向，需先取得更可靠的臨床資料才可評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

