---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 886
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Tocilizumab：預測新適應症為僵直性脊椎炎 (Ankylosing Spondylitis)（證據等級 L5）。原適應症：類風濕性關節炎、幼年型特發性關節炎、脊椎關節病變、顳動脈炎、Castleman 病、Kimura 病"
monitor_inn: "TOCILIZUMAB"
predicted_indications: ["ankylosing spondylitis", "rheumatoid vasculitis", "hypermobility of coccyx", "spondyloarthropathy, susceptibility to", "inflammatory spondylopathy"]
---

# Tocilizumab
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

# Tocilizumab：從類風濕性關節炎到僵直性脊椎炎

## 一句話總結

Tocilizumab 是一種抗介白素-6 受體（IL-6R）的單株抗體，原本用於類風濕性關節炎、幼年型特發性關節炎、顳動脈炎等疾病。
TxGNN 模型預測它可能對**僵直性脊椎炎 (Ankylosing Spondylitis)** 有效，但實際證據並不樂觀：目前有 **2 個已終止的 Phase 3 試驗**，以及多篇以回顧性文獻為主的資料。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、幼年型特發性關節炎、脊椎關節病變、顳動脈炎、Castleman 病、Kimura 病 |
| 預測新適應症 | 僵直性脊椎炎 (Ankylosing Spondylitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（形式上有 Phase 3 RCT，但兩項皆已終止） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tocilizumab 是 IL-6 受體拮抗劑，可阻斷 IL-6 所驅動的發炎訊號，在類風濕性關節炎等自體免疫疾病中的療效已獲證實。

IL-6 被認為參與脊椎關節病變的軸向發炎與骨重塑，因此從機轉上推測 IL-6R 阻斷可能適用於僵直性脊椎炎。TxGNN 的高分預測也反映了僵直性脊椎炎與其原適應症（如脊椎關節病變、類風濕性關節炎）在疾病網絡上的接近性。

不過，生物學上合理不等於臨床有效。已發表的文獻（包括 BUILDER-1 與 BUILDER-2 試驗分析）顯示，Tocilizumab 在僵直性脊椎炎中並未展現出令人信服的療效，表現不如 TNF 抑制劑與 IL-17 抑制劑。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | 已終止 | 113 | 雙盲安慰劑對照，用於對 TNF 拮抗劑反應不足的僵直性脊椎炎，比較 8 mg/kg、4 mg/kg 與安慰劑 |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | 已終止 | 306 | 雙盲安慰劑對照，用於 NSAID 失敗且未使用過 TNF 拮抗劑的僵直性脊椎炎 |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | 招募中 | 10000 | 韓國生物製劑登錄研究，屬觀察性，無針對本適應症的療效問題 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 招募中 | 80 | 風濕病患者肩關節置換術前後免疫抑制劑管理，非療效試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | 系統性回顧／網絡統合分析 | Medicine | 比較僵直性脊椎炎各種生物製劑的相對療效 |
| [36260501](https://pubmed.ncbi.nlm.nih.gov/36260501/) | 2022 | 系統性文獻回顧 | RMD Open | 為 IL-6 通路抑制劑的共識聲明提供療效與安全性證據 |
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT 結果分析 | Ann Rheum Dis | BUILDER-1 與 BUILDER-2 試驗評估 Tocilizumab 在僵直性脊椎炎的短期症狀療效 |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | 探討對 TNF 抑制劑無效的僵直性脊椎炎有哪些替代療法 |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | 簡述在僵直性脊椎炎中拮抗 IL-6 的角色 |
| [25488787](https://pubmed.ncbi.nlm.nih.gov/25488787/) | 2014 | Review | Best Pract Res Clin Rheumatol | 脊椎關節炎在 TNF 阻斷之外的治療選項 |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | 病例報告 | Front Med | 兩例僵直性脊椎炎合併 AA 類澱粉樣變性，使用 Tocilizumab 治療成功 |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | 系統性回顧（安全性） | Expert Rev Clin Immunol | 發炎性關節炎使用生物製劑與非生物製劑的感染風險比較 |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | 指引／Review | Front Immunol | 自體免疫關節炎使用生物製劑時的結核病風險管理 |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2017 | Review | Curr Pharm Biotechnol | 生物製劑於發炎性關節炎的應用 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59200 | ACTEMRA CONC FOR SOLN FOR INFUSION 400MG/20ML | 輸注濃縮液 | 未提供 |
| HK-63771 | ACTEMRA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 162MG/0.9ML | 預填充注射液 | 未提供 |
| HK-59202 | ACTEMRA CONC FOR SOLN FOR INFUSION 80MG/4ML | 輸注濃縮液 | 未提供 |
| HK-59201 | ACTEMRA CONC FOR SOLUTION FOR INF 200MG/10ML | 輸注濃縮液 | 未提供 |

以上 4 張許可證皆為單方製劑，持有廠商為 Roche Hong Kong Limited，狀態均為有效。

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，其中標示為「嚴重 (Major)」者包括 Deferiprone；「中度 (Moderate)」者包括 Warfarin、Apixaban、Rivaroxaban、Dicoumarol（抗凝血劑）、Simvastatin、Rosuvastatin（史他汀類）、Hydroxychloroquine、Chloroquine、Lidocaine、Naltrexone、Metronidazole、Disulfiram 等。鋅製劑（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）屬輕微 (Minor) 等級。
- **文獻中的安全訊號**：相關文獻提示生物製劑可能增加感染（含結核病）風險；另有病例報告顯示 Tocilizumab 治療後出現嚴重肝損傷，以及類血管炎的皮膚反應。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然有 2 個 Phase 3 試驗，但兩者皆提前終止，且已發表文獻顯示 Tocilizumab 在僵直性脊椎炎中缺乏令人信服的療效，不如 TNF 與 IL-17 抑制劑。因此證據等級雖形式上為 L1，實際並無正面療效訊號支持推進。
- 其他預測適應症也不建議優先推進：類風濕性血管炎僅有病例報告等間接證據（L4，列為研究問題）；尾骨過度活動度與脊椎關節病變易感性則缺乏機轉連結或屬於遺傳易感性術語，不是可治療的臨床疾病。

**若要推進需要：**
- 取得兩項已終止試驗的完整結果與終止原因。
- 若考慮特殊情境（如合併 AA 類澱粉樣變性的難治性病例），需累積更多前瞻性資料。
- 補齊作用機轉資料與香港仿單的警語及禁忌症資訊。
- 若有意探索類風濕性血管炎，需設計針對性研究，並評估文獻中提到的 Tocilizumab 誘發血管炎樣反應與肝損傷風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

