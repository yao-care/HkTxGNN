---
layout: default
title: Mercaptopurine
parent: 高證據等級 (L1-L2)
nav_order: 565
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Mercaptopurine：預測新適應症為骨髓性白血病 (Myeloid Leukemia)（證據等級 L2）。原適應症：急性淋巴芽細胞白血病"
---

# Mercaptopurine
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

# Mercaptopurine：從急性淋巴芽細胞白血病到骨髓性白血病

## 一句話總結

Mercaptopurine（6-MP）是嘌呤類抗代謝藥物，原本用於急性淋巴芽細胞白血病（含前驅 T 細胞型及急性前骨髓球性白血病等）的治療。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，
目前有 **14 個臨床試驗**和 **20 篇文獻**支持這個方向，但多數為多藥併用方案，無法單獨評估 mercaptopurine 的貢獻。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴芽細胞白血病（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠機轉欄位未收錄）。根據已知藥理，mercaptopurine 是嘌呤類抗代謝藥物，其代謝物（硫鳥嘌呤核苷酸）會嵌入 DNA 與 RNA，並抑制嘌呤的從頭合成，對快速增生的白血病母細胞具細胞毒性，且不限於淋巴系。

原適應症為急性淋巴芽細胞白血病，新適應症為骨髓性白血病，兩者同屬急性白血病，都是造血細胞的惡性增生。口服 6-MP 加 methotrexate 的維持治療，已在急性前骨髓球性白血病（APL）中被探討並作為維持方案的一部分，也有研究用於無法接受移植的 AML 患者。

需注意：目前檢索到的 Phase 3 試驗多為多藥併用方案，無法分離出 mercaptopurine 單獨的貢獻，因此這些資料不足以支持 L1 等級。

## 臨床試驗證據

以下列出最相關的 10 個試驗（共檢索到 14 個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | 進行中（不再招募） | 280 | 唐氏症患者 AML 的風險分層療法；為多藥方案，6-MP 角色不明 |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | 完成 | 105 | SWOG S0521：低中風險 APL 維持治療 vs 觀察；維持方案可能含 6-MP 與 methotrexate |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | 完成 | 133 | 高風險 APL：ATO + ATRA + idarubicin 對比 AIDA 方案 |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | 完成 | 238 | 新診斷 AML 兩種 cytarabine 劑量的多藥方案比較 |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | 未知 | 750 | ATRA + idarubicin 誘導，依微量殘存病灶隨機維持治療（APL） |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | 完成 | 420 | APL：tretinoin 間歇維持 vs tretinoin + mercaptopurine + methotrexate，並比較 arsenic trioxide |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | 完成 | 276 | 非高風險 APL：ATO + ATRA 對比 AIDA 方案 |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | 完成 | 106 | 兒童 APL 於鞏固期使用 arsenic trioxide 的風險調整治療 |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | 招募中 | 48 | AML/高風險 MDS 不適合標準治療者，hydroxyurea 或 6-MP 併用 valproic acid |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | 招募中 | 10 | 復發/難治 AML：venetoclax 併用 6-MP |

其中 NCT00003934 直接納入 mercaptopurine 加 methotrexate 的維持組，是相關性最高的設計。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | 無法移植的 AML 患者接受口服 6-MP + methotrexate 維持治療，觀察無白血病存活與整體存活 |
| [38828002](https://pubmed.ncbi.nlm.nih.gov/38828002/) | 2024 | Cohort | Ther Adv Hematol | 中國多中心兒童 AML，雙誘導加類 ALL 鞏固的強化化療 |
| [22715121](https://pubmed.ncbi.nlm.nih.gov/22715121/) | 2012 | Cohort | Blood | APML4：ATRA、idarubicin 與靜脈 ATO 作為 APL 初始治療 |
| [33183436](https://pubmed.ncbi.nlm.nih.gov/33183436/) | 2021 | Review | J Nanosci Nanotechnol | 6-MP 奈米藥物在白血病治療的應用，針對溶解度低與毒性大的問題 |
| [12057059](https://pubmed.ncbi.nlm.nih.gov/12057059/) | 2000 | Review | Curr Treat Options Oncol | APL 治療概述，ATRA 為誘導治療核心 |
| [34442422](https://pubmed.ncbi.nlm.nih.gov/34442422/) | 2021 | Review | J Pers Med | NUDT15 多型性對 thiopurine 治療的重要性（骨髓抑制風險） |
| [27275453](https://pubmed.ncbi.nlm.nih.gov/27275453/) | 2016 | 前瞻性先導研究 | South Asian J Cancer | 老年 AML 以口服 6-MP 進行節拍式化療 |
| [32459546](https://pubmed.ncbi.nlm.nih.gov/32459546/) | 2020 | 回溯性研究 | Pediatr Hematol Oncol | 幼年型骨髓單核球性白血病（JMML）接受 cytarabine 與 6-MP 序貫治療的結果 |
| [3513537](https://pubmed.ncbi.nlm.nih.gov/3513537/) | 1986 | 臨床研究 | Am J Clin Oncol | Hydroxyurea 併用 6-MP 治療慢性顆粒球性白血病 |
| [2676034](https://pubmed.ncbi.nlm.nih.gov/2676034/) | 1989 | Review | Blood Rev | 嘌呤代謝作為白血病化療標的，含 6-MP 與 6-thioguanine |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-03770 | PURI-NETHOL TAB | 錠劑（資料未載明） | 資料未載明 |
| HK-65479 | ALLMERCAP MERCAPTOPURINE ORAL SUSPENSION 20MG/ML | 口服懸液劑 | 資料未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤類抗代謝藥物） |
| 骨髓抑制風險 | 中至高（知識圖譜顯示與血小板減少、嗜中性球減少、白血球減少、顆粒球缺乏、貧血相關；NUDT15 / TPMT 多型性會增加風險） |
| 致吐性分級 | 低 |
| 監測項目 | CBC（含分類）、肝功能（含膽紅素）、腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細內容請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜標示的禁忌/需謹慎族群**（非仿單文字）：腎臟疾病、肝臟疾病、膽囊疾病、胰臟炎、膽汁鬱積（含良性復發性肝內膽汁鬱積、家族性肝內膽汁鬱積）、高膽紅素血症（含遺傳性）、Gilbert 症候群、血小板減少、嗜中性球減少、顆粒球缺乏、白血球減少、貧血（含巨球性貧血）、肝脾 T 細胞淋巴瘤、膿尿輸尿管。
- **藥物交互作用**：共查得 100 筆，以下為主要項目：
  - 中度：mesalazine、balsalazide、olsalazine、sulfasalazine（5-ASA 類）、naltrexone
  - 輕度：levofloxacin
  - 其他尚未分級者包括 prednisone、hydrocortisone、omeprazole、pantoprazole、lansoprazole、metformin、simvastatin、amphotericin B、vancomycin 等

香港仿單的警語與禁忌尚待取得，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個 Phase 3 試驗涵蓋 AML/APL 方案，其中部分含 mercaptopurine 維持治療，機轉合理且已有臨床使用經驗；但試驗多為多藥併用，無法判定 mercaptopurine 單獨的療效，故證據等級為 L2，不到 L1。
- 香港仿單的警語與禁忌資料尚缺，且骨髓抑制風險明確，需設置安全防護。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症
- 補充詳細的作用機轉資料（如 DrugBank）
- 針對 AML/APL 維持治療，設計能分離 mercaptopurine 貢獻的比較研究或次族群分析
- 建立 TPMT / NUDT15 基因型檢測與血液學監測計畫
- 評估與 5-ASA 類藥物併用時的骨髓抑制風險管理

---

**附註：其他預測適應症（證據不足，建議 Hold）**

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 慢性淋巴球性白血病/小淋巴球淋巴瘤（前生發中心型及 IGHV 突變型） | 99.84% | L5 | 僅有模型預測，無臨床試驗與文獻；mercaptopurine 在 CLL 無既定角色 |
| 肺母細胞瘤 (Pulmonary Blastoma) | 99.82% | L5 | 僅有模型預測，無機轉依據，且疾病極罕見 |
| 何杰金氏淋巴瘤 (Hodgkin's Lymphoma) | 99.80% | L4 | 所檢索試驗多為 ALL 與淋巴芽細胞性非何杰金氏淋巴瘤，屬間接證據；文獻多為 thiopurine 相關淋巴增生與 IBD 安全性，並非療效證據 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

