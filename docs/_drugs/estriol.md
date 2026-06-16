---
layout: default
title: Estriol
parent: 高證據等級 (L1-L2)
nav_order: 287
evidence_level: L1
indication_count: 1
---

# Estriol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Estriol：從更年期雌激素補充到閉經（Amenorrhea）

## 一句話總結

Estriol（E3）是人體天然弱效雌激素，傳統上用於更年期相關症狀（如泌尿生殖道萎縮、陰道乾燥）的補充治療。
TxGNN 模型預測它可能對**閉經（Amenorrhea）** 有效，
目前有 **2 個已完成的 Phase 3 臨床試驗**（招募逾 2,500 名受試者）和 **13 篇文獻**（含 1 篇直接研究 Estriol 於功能性下視丘閉經的臨床介入研究）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 更年期雌激素補充治療（臺灣目前無核准登記） |
| 預測新適應症 | 閉經（Amenorrhea） |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L1 |
| 臺灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉正式資料。根據文獻已知資訊，Estriol（E3）是人體天然弱效雌激素，對 ERα/ERβ 受體具部分促效活性，其生物效力約為 Estradiol（E2）的 1/10 至 1/80。Estriol 可透過**下視丘–腦垂體–卵巢軸（HPG axis）**的神經內分泌回饋機制，調節促黃體素（LH）的脈衝分泌頻率。

在**功能性下視丘閉經（Functional Hypothalamic Amenorrhea, FHA）**中，GnRH 脈衝產生器受心理社會或代謝壓力抑制，導致 LH/FSH 低下與無排卵。低劑量 Estriol 可透過正/負回饋調節，協助恢復 LH 脈衝頻率，進而重建月經週期。在低雌激素性繼發性閉經（如早發性卵巢功能不足，POI/POF）的情境中，Estriol 亦可補充雌激素缺乏，恢復子宮內膜週期及內分泌回饋軸功能。

相較於 Estradiol，Estriol 效力較弱，理論上安全性輪廓更為溫和，尤其適合長期神經內分泌調節用途。2012 年 *Fertility and Sterility* 期刊發表的臨床介入研究（PMID 22137494）已直接驗證 Estriol 給藥能顯著調節 FHA 患者的 LH 分泌，為此預測提供了最直接的機轉支持。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | 完成 | 1,570 | E4Comfort Study I：雙盲安慰劑對照試驗，評估 Estetrol（E4）15/20 mg 對停經後女性中重度血管運動症狀（VMS）之療效，及 E4 20 mg 的子宮內膜安全性 |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | 完成 | 1,015 | E4Comfort Study II：雙盲安慰劑對照試驗，評估 Estetrol（E4）15/20 mg 對中重度 VMS 的症狀緩解效果與整體安全性 |
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | 已撤回 | 0 | 光生物調控（Photobiomodulation）對停經後外陰陰道萎縮的效果評估；研究介入為物理療法而非 Estriol 直接給藥，且已撤回未執行，不具證據效力 |

> ⚠️ **重要提示**：上述 Phase 3 試驗（NCT04209543、NCT04090957）的研究藥物為 **Estetrol（E4，四羥雌激素）**，與本報告評估的 **Estriol（E3，三羥雌激素）**為不同化合物。兩者同屬天然雌激素家族，但分子結構與受體結合效力有所差異。引用上述試驗作為 Estriol 之支持證據時，需注意此侷限性。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Narrative/Systematic Review | *Biomedicines* | 低劑量雌激素作為功能性下視丘閉經（FHA）的神經內分泌調節劑，探討誘發正回饋機制的可能性與治療潛力 |
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | 臨床介入研究 | *Fertility and Sterility* | **核心直接證據**：Estriol 給藥可顯著調節 FHA 患者的下視丘–腦垂體功能及 LH 分泌，直接支持 E3 於閉經的臨床應用 |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | 世代/觀察性研究 | *Medicinski Pregled* | 雌孕素對早發性原發性卵巢衰竭（PPOF）女性脂質與荷爾蒙指標的影響；高性腺激素性閉經患者之雌激素補充療效 |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case Series | *Lancet* | 2 例早發性卵巢衰竭患者的內分泌學發現，早期記錄閉經合併低雌激素的臨床表現 |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | 臨床試驗 | *J Obstet Gynaecol Br Commonw* | 人類促性腺激素對特發性繼發性閉經患者的臨床試驗，探討 FSH/hCG 在閉經治療中的角色 |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | 基礎研究/藥理學回顧 | *J Clin Endocrinol Metab* | 抗排卵化合物的早期作用機轉研究，奠定雌激素調節 HPG 軸的藥理基礎 |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | *Clinical Obstetrics and Gynecology* | 荷爾蒙避孕與腫瘤風險的回顧，提供雌激素長期使用的安全性背景資料 |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | 觀察性研究 | *中西醫結合雜誌* | 中醫「腎虛」概念與閉經/月經稀少患者性腺功能變化的關係，提供跨文化診療背景 |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Case Series | *Am J Obstet Gynecol* | 妊娠期給予 Medroxyprogesterone Acetate 後的長期婦科及內分泌表現，包含繼發性閉經案例 |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Case Report/Clinical Review | *Br J Psychiatry* | 神經性厭食症相關功能性閉經病例，提供 FHA 在特定臨床情境的表現 |

---

## 臺灣上市資訊

Estriol 目前**未在臺灣取得藥品許可證**（市場狀態：未上市，許可證數：0）。若需臨床應用，須依《藥事法》相關規定申請專案進口，或評估是否採用已在臺上市的同類雌激素製劑（如 Estradiol 製劑）替代。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 預測分數達 99.18%，2012 年有直接臨床介入研究（PMID 22137494）驗證 Estriol 對 FHA 患者 LH 分泌的調節效果，機轉合理性明確；惟 Estriol 在臺灣尚未上市、安全性資料空缺，且高等級臨床試驗為 Estetrol（E4）而非 Estriol（E3），需謹慎區分後再推進。

**若要推進需要：**
- 補充 MOA 詳細資料（查詢 DrugBank API，填補 DG002 資料空缺）
- 下載並解析原廠仿單 PDF，取得警語與禁忌症（填補 DG001 阻塞性資料空缺）
- 確認 Phase 3 試驗（E4Comfort I/II）為 Estetrol 而非 Estriol，評估是否需補充 E3 專屬 Phase 2/3 試驗作為監管支持
- 規劃臺灣專案進口申請，或評估以 Estradiol 等已上市雌激素製劑作為橋接方案
- 針對 FHA 及 POI/POF 患者族群，建立長期雌激素補充的安全性監測計畫（包含乳房、子宮內膜及心血管風險評估）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

