---
layout: default
title: Hyaluronidase
parent: 高證據等級 (L1-L2)
nav_order: 375
evidence_level: L1
indication_count: 10
---

# Hyaluronidase
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

以下是根據 Evidence Pack 生成的評估報告：

---

# Hyaluronidase：從眼科擴散輔助劑到糖尿病視網膜病變

> **選擇說明**：TxGNN 最高分預測為 esotropia（斜視，rank 2904），但 repurposing_rationale 已明確指出該預測可能為眼科節點共現的誤導性高分，且無任何臨床或文獻支持。本報告聚焦於證據最強的預測目標——**糖尿病視網膜病變（rank 6091）**，此適應症具備 L1 證據等級（2 個獨立完成的 Phase 3 RCT）。

## 一句話總結

Hyaluronidase 是一種天然 HA 降解酵素，目前獲 FDA 核准作為眼科擴散輔助劑（Vitrase®，2004 年），用於促進局部麻醉藥物擴散及分解玻尿酸填充物。TxGNN 模型預測它可能對**糖尿病視網膜病變 (Diabetic Retinopathy)** 有效，目前有 **3 個臨床試驗**（包含 2 個已完成的 Phase 3 大型 RCT，合計受試者 1,260 人）和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 眼科擴散輔助劑（局部麻醉輔助注射，FDA 核准 2004） |
| 預測新適應症 | 糖尿病視網膜病變 (Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市（0 張許可證） |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Hyaluronidase 的核心作用機轉是水解玻尿酸（Hyaluronic Acid, HA）多醣鏈，透過降解 HA 來降低組織黏稠度。在眼科場景中，玻璃體腔含有大量 HA；Hyaluronidase 玻璃體內注射後，可降低玻璃體黏稠度、誘發後玻璃體分離（Posterior Vitreous Detachment, PVD），並促進玻璃體出血液化吸收，此過程稱為「藥理性玻璃體溶解（Pharmacologic Vitreolysis）」。

糖尿病視網膜病變——尤其是增殖型（PDR）——最終常伴隨玻璃體出血，是糖尿病患者視力喪失的主要原因之一。傳統治療為玻璃體切除手術（vitrectomy），屬侵入性操作且存在術後併發症風險。Hyaluronidase 提供了非手術的藥理替代路徑。最新機轉研究（PMID 41789111，2026）更直接發現，PDR 患者眼內微環境中 HA 合成酶（HAS-2）上調、Hyal-1/Hyal-2 失調，導致 HA 異常堆積，進而驅動發炎與病理性血管新生，進一步支持此機轉假說。

兩個獨立的 Phase 3 RCT（合計 n＝1,260）驗證了 Vitrase® 於嚴重玻璃體出血（主要見於 PDR）的療效概念，顯示機轉轉化至臨床有明確依據。需注意：FDA 雖核准 Vitrase® 為眼科擴散劑，但玻璃體出血清除之特定適應症於 Phase 3 後未獲 FDA 最終核准，監管狀態與臨床試驗結果需分開解讀。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | 完成 | 750 | 評估 Vitrase（ovine hyaluronidase）玻璃體內注射清除嚴重玻璃體出血的安全性與療效，為本藥最高等級臨床證據 |
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | 完成 | 510 | 獨立驗證 Vitrase 玻璃體內注射用於嚴重玻璃體出血；與 NCT00198510 構成雙重 Phase 3 證據基礎 |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | 完成 | 10 | 開放性評估 Vitrase 誘發後玻璃體分離（PVD）於中至重度非增殖型糖尿病視網膜病變患者的療效；規模小，作為先導研究參考 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | Mechanistic Study | Frontiers in Immunology | PDR 眼內 HA 代謝失調（HAS-2↑、Hyal-1/2 失衡），HA 異常堆積驅動眼內發炎與血管新生，直接支持 hyaluronidase 機轉靶點 |
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Current Pharmaceutical Biotechnology | 綜述藥理性玻璃體溶解於糖尿病視網膜病變的應用，確認 intravitreal ovine hyaluronidase 可有效清除玻璃體出血 |
| [19199900](https://pubmed.ncbi.nlm.nih.gov/19199900/) | 2009 | Review | Current Diabetes Reviews | 酵素性玻璃體溶解：hyaluronidase 可誘發 PVD，改善 PDR 及糖尿病黃斑水腫，總結當時研究進展 |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | Mechanistic Study | Investigative Ophthalmology & Visual Science | 酵素誘發玻璃體溶解透過 HIF-1α 路徑減緩糖尿病視網膜病變進展之機轉研究 |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | Animal Study | Retina | 糖尿病大鼠中 plasmin 與 hyaluronidase 合用誘發 PVD 的藥理性玻璃體溶解可行性與安全性 |
| [30445048](https://pubmed.ncbi.nlm.nih.gov/30445048/) | 2019 | Animal Study | Experimental Eye Research | 評估糖尿病與 hyaluronidase 對小鼠視網膜內皮糖萼厚度的影響，探討視網膜屏障相關機轉 |
| [17245084](https://pubmed.ncbi.nlm.nih.gov/17245084/) | 2007 | Review | Developments in Ophthalmology | 藥理性玻璃體溶解完整綜述：完全 PVD 有助改善糖尿病視網膜病變、黃斑病變等多種視網膜疾病 |
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Experimental Diabetes Research | 糖尿病視網膜病變藥理治療的現況與未來，涵蓋 hyaluronidase 作為輔助治療角色的討論 |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Drug Review | Drugs in R&D | Vitrase（ISTA Pharmaceuticals）用於玻璃體出血及糖尿病視網膜病變初步治療的藥物開發綜述 |
| [19576064](https://pubmed.ncbi.nlm.nih.gov/19576064/) | 2009 | Animal Study | Chinese Journal of Ophthalmology | 評估 plasmin 或 hyaluronidase 於糖尿病大鼠誘發 PVD 的效果與安全性，中文期刊資料 |

## 安全性考量

安全性資訊請參考原廠仿單。

> **補充注意**：文獻 PMID 37145319（2024，Aesthetic Plastic Surgery）記錄 hyaluronidase 注射本身可能引發過敏性併發症（自 1984 年起有案例報告），於玻璃體內給藥前應考量過敏評估。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Hyaluronidase 透過玻璃體 HA 降解誘發 PVD 的機轉，在糖尿病視網膜病變（PDR 玻璃體出血）場景中具直接病理生理合理性，且獲兩個獨立完成的 Phase 3 大型 RCT 支持（合計 n＝1,260）。然而，FDA Phase 3 完成後未核准玻璃體出血特定適應症，現行 FDA 核准範圍僅限擴散輔助劑；香港目前亦無上市許可，需先釐清監管路徑。

**若要推進需要：**
- 調查 FDA 未核准玻璃體出血適應症的具體原因（有效性未達標？安全性顧慮？），評估監管風險
- 向 HKSAR 衛生署申請前，先確認 Hyaluronidase 注射劑在香港的監管分類與進口途徑
- 取得 Vitrase® 原廠仿單（FDA label），完整評估安全性警語、禁忌症與眼科注射相關風險
- 查詢 DrugBank DB14740 補全 MOA 資料，強化機轉分析深度
- 確認給藥途徑（玻璃體內注射）的眼科專科執行要求與監測計畫
- 參考最新機轉研究（PMID 41789111，2026）評估是否有設計 NPDR 階段的新研究機會
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

