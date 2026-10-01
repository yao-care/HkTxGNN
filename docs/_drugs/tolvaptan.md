---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 874
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan：從原適應症（資料未載明）到多囊腎病 3 型（伴或不伴多囊肝）

## 一句話總結

Tolvaptan 是選擇性血管加壓素 V2 受體拮抗劑，本次資料未載明其原適應症。
TxGNN 模型預測它可能對**多囊腎病 3 型，伴或不伴多囊肝 (Polycystic kidney disease 3 with or without polycystic liver disease)** 有效。
目前**無登記中的臨床試驗**，但有 **20 篇文獻**，其中包含 2 篇 ADPKD 的 RCT（TEMPO 3:4 與 REPRISE），不過針對 PKD3 基因型的證據屬間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 多囊腎病 3 型，伴或不伴多囊肝 (Polycystic kidney disease 3 with or without polycystic liver disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（依 Evidence Pack 評分；證據來自 ADPKD 的 RCT，屬間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Tolvaptan 是選擇性血管加壓素 V2 受體拮抗劑。在 ADPKD 中，它能降低囊腫上皮細胞的 cAMP 訊號，進而減緩囊腫生長與總腎體積增加。目前缺乏 DrugBank 的詳細作用機轉資料，以上說明來自預測的機轉推論。

PKD3（與 GANAB 相關）和 PKD1/PKD2 共享 polycystin 路徑的囊腫形成生物學，因此機轉上可能適用。

有一點要特別留意：Tolvaptan 在 ADPKD 已上市，且獲指引背書，所以這不是典型的老藥新用訊號。Evidence Pack 中空白的原適應症與 MOA 欄位，很可能是資料缺口。TEMPO 3:4 與 REPRISE 收錄的是未依 GANAB 基因型分層的 ADPKD 族群，因此對 PKD3 基因型及多囊肝部分的證據都是間接的。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | TEMPO 3:4：V2 受體拮抗劑 tolvaptan 用於 ADPKD，臨床前研究顯示可抑制囊腫生長並減緩腎功能下降 |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | 評估 tolvaptan 用於晚期 ADPKD 的療效與安全性，先前早期 ADPKD 試驗曾見轉胺酶與膽紅素升高 |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | 隨機試驗（事後分析） | Pediatr Nephrol | 兒童 ADPKD（5-17 歲）tolvaptan 試驗（NCT02964273）參與者的快速進展風險回溯評估 |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | 系統性回顧與統合分析 | Nefrologia | 評估 tolvaptan 治療 ADPKD 的療效與安全性，指出可延緩進展至末期腎病 |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | 系統性回顧 | Cochrane Database Syst Rev | 回顧預防 ADPKD 進展的介入措施，涵蓋針對疾病機轉的新藥 |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | 共識聲明 | Nephrol Dial Transplant | ERA 等團體針對 tolvaptan 用於 ADPKD 的起始與長期治療提出共識 |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | 指引 | J Hepatol | EASL 囊性肝病處置指引，涵蓋多囊肝 |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD 綜述，是最常見的遺傳性腎臟疾病 |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | 多囊腎/肝病綜述，提及 tolvaptan 可減緩 ADPKD 腎功能惡化與囊腫生長 |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | 指出 tolvaptan 仍是唯一獲 FDA 核准的 ADPKD 疾病進展療法，並整理新興療法 |

以上文獻皆針對 ADPKD 或多囊肝，沒有專門針對 PKD3（GANAB）基因型的 tolvaptan 研究。

## 香港上市資訊

共 7 張許可證，以下列出 5 張主要許可證（廠商皆為 OTSUKA PHARMACEUTICAL (H.K.) LIMITED）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59911 | SAMSCA TAB 30MG | 資料未載明 | 資料未載明 |
| HK-65102 | JINARC TABLETS 60MG + 30MG | 資料未載明 | 資料未載明 |
| HK-65101 | JINARC TABLETS 15MG | 資料未載明 | 資料未載明 |
| HK-65099 | JINARC TABLETS 90MG + 30MG | 資料未載明 | 資料未載明 |
| HK-65098 | JINARC TABLETS 30MG | 資料未載明 | 資料未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Tolvaptan 在 ADPKD 已有 2 項大型 RCT 與多份指引、共識支持，且機轉（降低 cAMP）可合理延伸到共享 polycystin 路徑的 PKD3。但 PKD3 基因型與多囊肝部分的證據都是間接的，且已知有藥物性肝損傷風險，因此需設防護條件才能推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症（目前為阻斷性資料缺口）
- 補齊 DrugBank 的作用機轉資料
- 尋找或設計 GANAB 相關 PKD3 及多囊肝族群的直接證據
- 以快速進展標準篩選病人，並定期監測肝功能
- 管理排水利尿與高血鈉風險

**其他預測適應症：**
- Joubert 症候群伴腎臟缺損（腎消耗病）有合理的 cAMP 機轉，列為研究問題（Research Question）。
- 其餘預測適應症缺乏證據或機轉連結，皆建議 Hold。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

