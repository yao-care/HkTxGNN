---
layout: default
title: Vinorelbine
parent: 高證據等級 (L1-L2)
nav_order: 938
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Vinorelbine：預測新適應症為尤文氏肉瘤 (Ewing sarcoma)（證據等級 L2）。原適應症：非小細胞肺癌、肺癌"
---

# Vinorelbine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Vinorelbine：從非小細胞肺癌到尤文氏肉瘤

## 一句話總結

Vinorelbine（長春瑞濱）是一種長春花生物鹼類化療藥物，原本用於非小細胞肺癌（肺癌）治療。
TxGNN 模型預測它可能對**尤文氏肉瘤 (Ewing sarcoma)** 有效，
目前有 **3 個臨床試驗**和 **6 篇文獻**支持這個方向，其中以 Phase 2 研究為主。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、肺癌（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 尤文氏肉瘤 (Ewing sarcoma) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥物類別，Vinorelbine 是長春花生物鹼，可抑制微管聚合，造成有絲分裂停滯並誘發細胞凋亡，主要作用於快速分裂的細胞。

尤文氏肉瘤是增殖活躍的惡性骨腫瘤，復發率高，尤其是多處轉移的病人。抗有絲分裂的機轉在理論上適用於這類腫瘤。前臨床研究（PMID 26260582）也顯示，微管干擾藥物（含 vinorelbine）與 PLK1 抑制劑在尤文氏肉瘤細胞中有協同誘導凋亡的效果。

臨床上，Vinorelbine 搭配低劑量持續（節拍式）cyclophosphamide，已在復發或難治的兒童肉瘤中顯示活性。2026 年的系統性回顧也以此組合作為國際 INTER-EWING-1 試驗維持治療的立論基礎。需注意，這個機轉連結來自藥物類別的已知機轉，並非來自本報告所整理的藥物專屬資料。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | 完成 | 50 | Vinorelbine 用於兒童復發或難治性惡性腫瘤；腫瘤類型混合，尤文氏肉瘤專屬證據有限，未提供結果 |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | 狀態未知 | 210 | Vinorelbine + cyclophosphamide 用於難治或復發腫瘤（含尤文氏瘤、橫紋肌肉瘤等）；組合與文獻相符，但無結果 |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | 不適用 | 進行中（不招募） | 100 | 中國兒童尤文氏肉瘤風險分層治療的前瞻性世代研究；僅提供背景與安全性資料，並非直接檢驗療效 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 試驗 | Eur J Cancer | Vinorelbine 合併持續低劑量 cyclophosphamide 用於復發或難治實體瘤的兒童與年輕成人，耐受性良好，在橫紋肌肉瘤中有療效 |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase 2 試驗 | Cancer | Vinorelbine 用於曾接受治療的晚期兒童肉瘤，在橫紋肌肉瘤中顯示活性 |
| [42561548](https://pubmed.ncbi.nlm.nih.gov/42561548/) | 2026 | 世代／系統性回顧 | Cancer Treat Rev | 回顧維持治療在尤文氏肉瘤的可行性，作為 INTER-EWING-1 試驗選藥（含 vinorelbine + 低劑量 cyclophosphamide）的依據 |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Front Pharmacol | 軟組織肉瘤化療藥物綜述 |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | 前臨床 | Int J Cancer | PLK1 抑制劑與微管干擾藥物（含 vinorelbine）在尤文氏肉瘤細胞中協同誘導凋亡 |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case report | BMC Urol | 腎臟骨外尤文氏肉瘤的個案報告與文獻回顧，與 vinorelbine 療效關聯有限 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67132 | VINORELBINE ALVOGEN CAPSULES 20MG（Lotus Pharmaceutical） | 膠囊 | 未提供 |
| HK-67133 | VINORELBINE ALVOGEN CAPSULES 30MG（Lotus Pharmaceutical） | 膠囊 | 未提供 |
| HK-60311 | VINORELBIN EBEWE CONC FOR SOLN FOR INF 10MG/ML（Sandoz） | 輸注濃縮液 | 未提供 |
| HK-60888 | VINORELBINE TARTRATE INJECTION 10MG/ML（Jindun Pharma） | 注射劑 | 未提供 |
| HK-56213 | NAVELBINE CAP 30MG（Pierre Fabre） | 膠囊 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（長春花生物鹼類，微管抑制劑） |
| 骨髓抑制風險 | 高（知識圖譜顯示白血球低下為禁忌相關疾病，使用前須確認血球數） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自知識圖譜，非仿單文字）：肝衰竭、感染性疾病、腸阻塞（ileus、intestinal obstruction）、間質性肺病、肺部疾病、白血球低下。
- **藥物交互作用**：共查得 100 筆，以下為主要項目：
  - 重大（Major）：Clarithromycin
  - 中度（Moderate）：Aprepitant、Dexamethasone、Metronidazole、Eliglustat、Miconazole、Rolapitant、Rosuvastatin、Simvastatin、Tinidazole、Glycerol phenylbutyrate
  - 輕微（Minor）：Levofloxacin

香港仿單的警語與禁忌尚未取得，詳細資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 個 Phase 2 試驗與數篇 Phase 2 文獻支持 vinorelbine（尤其合併低劑量 cyclophosphamide）用於復發或難治兒童肉瘤，且 2026 年的國際試驗已採用此組合作為維持治療依據。
- 但這些研究多為混合腫瘤類型，尤文氏肉瘤專屬的療效結果有限，且缺乏已完成的 Phase 3 RCT，所以屬於 L2，建議在防護措施下推進。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症（目前為阻擋性資料缺口）
- 補充 vinorelbine 的作用機轉資料（如 DrugBank）
- 取得 NCT00003234 與 NCT00180947 的結果，並追蹤 INTER-EWING-1 試驗進展
- 制定血液學監測與劑量調整計畫，並評估兒童族群與 CYP3A4 交互作用（如 clarithromycin）的風險

**其他預測適應症備註：**
- 肺溝腫瘤（Pancoast 腫瘤）：證據等級 L4，本質上屬於原適應症（非小細胞肺癌）的延伸，證據未顯示 vinorelbine 的特定貢獻，列為研究問題。
- 肺生殖細胞瘤：L4，現有證據屬間接，建議 Hold。
- 牙齦纖維瘤病、肺纖維瘤：僅有模型預測、無臨床證據（L5），機轉上無明顯依據，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

