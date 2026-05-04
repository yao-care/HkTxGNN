---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept：從眼科血管新生抑制到內斜視 (Esotropia)

## 一句話總結

Aflibercept 是一種 VEGF 抑制劑（抗血管新生融合蛋白），國際上以 Eylea 品牌廣泛用於濕性老年性黃斑部病變（wet AMD）、糖尿病黃斑水腫等眼科疾病，但目前在香港**尚未取得上市許可**。
TxGNN 模型預測其最高分適應症為**內斜視 (Esotropia)**，預測分數高達 **99.38%**，然而此預測**完全無臨床試驗或文獻支持**，10 項預測全部建議 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 濕性 AMD、糖尿病黃斑水腫（國際核准；香港未上市） |
| 預測新適應症（第 1 名） | 內斜視 (Esotropia) |
| TxGNN 預測分數 | 99.38%（排名第 10,400） |
| 證據等級 | L5（僅模型預測） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold**（全部 10 項預測均為 Hold） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據已知的國際資訊，Aflibercept 是一種重組融合蛋白，作為 VEGF-A、VEGF-B 及 PlGF 的誘餌受體（decoy receptor），透過強力競爭性結合阻斷 VEGF 訊號通路，抑制異常血管新生（pathological angiogenesis）。

**關於內斜視的預測合理性有限**。內斜視由眼外肌協調異常或神經支配失調所致，並非血管新生異常。雖然部分研究探討 VEGF 在眼外肌發育中的角色，但目前尚無明確證據連結 VEGF 抑制與斜視矯正。TxGNN 高預測分數可能反映的是知識圖譜中「眼科領域節點共現」的間接聯繫，而非直接機轉依據。

綜觀 10 項預測，其中食道靜脈曲張（ranks 2-3）、靜脈曲張病（rank 4）在機轉上有 VEGF 參與血管新生的理論基礎；稀有腫瘤（ranks 8-10）有廣義抗腫瘤血管生成假說；但尿道結石（rank 5）、腺苷脫氨酶缺乏症（rank 6）、新生兒出血症（rank 7）的預測合理性極低，疑為知識圖譜遠端路徑推斷的假陽性。

---

## 所有預測適應症總覽

| 排名 | 疾病（英文） | 疾病（中文） | TxGNN 分數 | 證據等級 | 決策 | 機轉合理性 |
|------|-------------|-------------|-----------|---------|------|----------|
| 1 | Esotropia | 內斜視 | 99.38% | L5 | Hold | ⚠️ 低（眼科共現，非直接機轉） |
| 2 | Esophageal varices with bleeding | 食道靜脈曲張（出血型） | 97.56% | L5 | Hold | ⚠️ 理論存在，給藥途徑不適用 |
| 3 | Esophageal varices without bleeding | 食道靜脈曲張（非出血型） | 97.56% | L5 | Hold | ⚠️ 理論存在，給藥途徑不適用 |
| 4 | Varicose disease | 靜脈曲張病 | 96.95% | L5 | Hold | ⚠️ 理論存在，全身暴露量不足 |
| 5 | Urethral calculus | 尿道結石 | 95.97% | L5 | Hold | ❌ 極低（與 VEGF 無已知關聯） |
| 6 | Adenosine deaminase deficiency | 腺苷脫氨酶缺乏症 | 95.76% | L5 | Hold | ❌ 極低（代謝途徑無交集） |
| 7 | Hemorrhagic disease of newborn | 新生兒出血症 | 95.56% | L5 | Hold | ❌ 極低（凝血機制無關聯） |
| 8 | Ectomesenchymoma | 外胚層間充質瘤 | 94.52% | L5 | Hold | ⚠️ 廣義腫瘤抗血管新生，罕見病 |
| 9 | Malignant cutaneous granular cell skin tumor | 惡性皮膚顆粒細胞腫瘤 | 94.51% | L5 | Hold | ⚠️ 廣義腫瘤抗血管新生，極罕見 |
| 10 | Middle ear neuroendocrine tumor | 中耳神經內分泌腫瘤 | 94.42% | L5 | Hold | ⚠️ 富血管腫瘤，有間接參考依據 |

---

## 臨床試驗證據

針對排名第 1 的預測適應症（內斜視）：目前**無相關臨床試驗登記**。

**附注**：排名第 7（新生兒出血症）有 1 筆臨床試驗記錄（[NCT02537054](https://clinicaltrials.gov/study/NCT02537054)），但經評估為**資料庫疾病分類錯誤**——該試驗實為研究 Aflibercept 治療假性黃色瘤（PXE）患者的脈絡膜新生血管（CNV）之 Phase 2 研究，與新生兒出血症完全無關，**不構成任何有效證據**，應歸類至眼科 CNV 適應症。

其餘 9 項預測適應症均無任何相關臨床試驗登記。

---

## 文獻證據

10 項預測適應症均**目前無相關文獻**。

---

## 香港上市資訊

Aflibercept 目前在香港**尚未取得上市許可**，無任何已登記許可證。

> 參考資訊：Aflibercept 在國際市場以 **Eylea**（玻璃體內注射劑）和 **Zaltrap/Ziv-aflibercept**（靜脈注射劑，用於大腸直腸癌）上市，已獲 US FDA、EMA 等主要藥管機構核准多項眼科及腫瘤科適應症。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **資料缺口（DG001）**：TFDA/香港衛生署仿單警語及禁忌資料目前缺失（嚴重度：Blocking）。補救建議：下載 TFDA 或 HKDOH 官方仿單 PDF 並解析相關欄位後，方可進入正式安全性初評（S1）。

---

## 結論與下一步

**決策：Hold（全面）**

**理由：**
10 項 TxGNN 預測適應症全部為 L5 等級（僅模型預測，無任何臨床試驗或文獻支持），且半數預測（尿道結石、ADA 缺乏症、新生兒出血症等）的生物學合理性極低，疑似知識圖譜假陽性；香港亦無上市許可，安全性資料缺口達 Blocking 等級，目前不具推進再利用評估的條件。

機轉上較有潛力的方向（食道/下肢靜脈曲張、稀有腫瘤）受限於給藥途徑限制（Aflibercept 為玻璃體內注射劑型，全身暴露量極低）及商業可行性，短期內亦難以推進。

**若要推進需要：**
1. **補齊安全性資料（DG001-Blocking）**：取得原廠仿單警語與禁忌症，完成 S1 安全性初評
2. **補齊 MOA 資料（DG002-High）**：查詢 DrugBank API 獲取完整作用機轉說明，重新評估機轉關聯性
3. **針對眼科腫瘤方向**（ectomesenchymoma、middle ear NET）：確認是否有 Bevacizumab 等同類藥物的間接臨床證據，作為平行參考
4. **靜脈曲張方向若要推進**：需評估全新給藥途徑（靜脈注射或局部內視鏡給藥）的可行性，涉及製劑重新開發，屬高投資低勝算路徑
5. **香港上市申請前提**：建議先確認國際市場（FDA/EMA）核准適應症是否可作為本地上市橋接基礎

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴格臨床驗證才能應用於實際醫療決策。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

