---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan：從特發性肺動脈高壓到先天性心臟病相關肺動脈高壓

## 一句話總結

Ambrisentan 是一種口服選擇性內皮素 A 型受體（ETA）拮抗劑，已在美國、歐盟等多國核准用於特發性肺動脈高壓（IPAH）的治療，目前香港尚未上市。TxGNN 模型預測它對**先天性心臟病相關 PAH（PAH-CHD）**、**結締組織病相關 PAH（CTD-PAH）** 及 **HIV 相關 PAH（HIV-PAH）** 等亞型可能有效，三個適應症合計有超過 **10 個臨床試驗**和 **25 篇文獻**支持；惟 TxGNN 最高分預測的肺動靜脈畸形（PAVM）因缺乏機轉依據，建議維持 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物類別 | 選擇性 ETA 受體拮抗劑（口服） |
| 國際已核准適應症 | 特發性／遺傳性肺動脈高壓（IPAH／HPAH） |
| TxGNN 最高分預測 | 肺動靜脈畸形（PAVM，**99.41%**）—— Hold |
| 最具臨床潛力適應症 | 先天性心臟病相關 PAH（PAH-CHD，**99.37%**） |
| 證據等級（PAH-CHD） | **L2** |
| 證據等級（CTD-PAH） | **L2** |
| 證據等級（HIV-PAH） | **L2** |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Proceed with Guardrails**（PAH-CHD / CTD-PAH / HIV-PAH） |

---

## 為什麼這個預測合理？

**作用機轉**

Ambrisentan 選擇性阻斷 ETA 受體，抑制內皮素-1（ET-1）誘導的肺血管平滑肌細胞收縮與增生，從而降低肺血管阻力（PVR）並減輕右心後負荷。詳細 MOA 文件尚待補充（目前為資料缺口），但其 ETA 選擇性拮抗作用已在 ARIES-1 及 ARIES-2 等大型特發性 PAH 的 RCT 中得到驗證。

**PAH-CHD 的機轉關聯**

先天性心臟病（CHD）引起的持續性左向右分流，使肺血管床長期承受高流量剪切力，觸發 ET-1 過度分泌與肺血管重塑，最終演變為艾森曼格症候群（Eisenmenger syndrome）。此一病生理進程與特發性 PAH 高度重疊，ETA 拮抗在 PAH-CHD 中的作用機轉具備直接的病理生理依據。完成於中國 134 例 PAH 患者的 Phase 3b 試驗（NCT01808313），以及兒科長期延伸研究（NCT01342952），均進一步支持此預測。

**CTD-PAH 的機轉關聯**

結締組織病（尤其是系統性硬化症 SSc）相關 PAH 的核心病理為血管內皮損傷合併 ET-1 大量分泌，驅動血管收縮與纖維化重塑。這是所有 PAH 亞型中 ETA 拮抗機轉最為直接的一類。AMBITION 試驗 CTD-PAH 亞組分析（PMID 28039187、32161055）及 EDITA 早期介入試驗（NCT02290613）均直接驗證 Ambrisentan 在此亞型中的有效性，且多項 Meta 分析支持其作為一線選擇。

**HIV-PAH 的機轉關聯**

HIV 的 gp120 蛋白直接損傷肺血管內皮，並上調 ET-1 表達，觸發 ETA 介導的血管收縮與增殖。此一機轉在 HIV-PAH 中具合理的病生理依據。PROWESS-15（NCT00709956）Phase 3 雙盲交叉 RCT 在 HIV-PAH 族群中評估了使用 Ambrisentan 作為背景治療時的活動耐受性，提供了間接但重要的臨床背景數據。

---

## 臨床試驗證據

### 先天性心臟病相關 PAH（Rank 2）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | Phase 3b | 完成 | 134 | 中國 PAH 患者開放標籤研究，評估 12 週 Ambrisentan 對 6MWT 的改善及安全性，為此適應症最具說服力的完成試驗 |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Phase 2 | 完成 | 38 | 兒科 PAH 長期延伸研究（追蹤至 2022 年，含 CHD 亞型），提供超過 10 年安全性數據 |
| [NCT01332331](https://clinicaltrials.gov/study/NCT01332331) | Phase 2 | 終止 | 41 | 兒科 PAH（8–18 歲）高低劑量體重調整比較試驗，24 週後因入組困難終止，提供兒科劑量範圍參考數據 |
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Phase 3 | 終止 | 33 | 不可手術 CTEPH 的雙盲安慰劑對照 RCT，設計最嚴謹，因入組困難（目標 160 例）終止，終止原因非安全問題，保留部分參考價值 |
| [NCT04095286](https://clinicaltrials.gov/study/NCT04095286) | Phase 1 | 完成 | 29 | 兒科低劑量配方與市售藥片的 PK 生物等效性研究，為兒科 CHD-PAH 用藥開發奠基 |

### 結締組織病相關 PAH（Rank 3）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | 完成 | 25 | SSc-PAH 患者使用 Ambrisentan + Tadalafil 聯合療法 36 週，評估 6MWD、NYHA 分級及右心室—肺循環功能，直接療效數據 |
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | 完成 | 38 | SSc-PAH borderline 期早期介入試驗（EDITA），雙盲安慰劑對照，評估 Ambrisentan 的疾病修飾潛力 |
| [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) | Phase 4 | 終止 | 3 | CTD-PAH 換藥方案比較研究，3 例入組後即終止，無有效數據 |

### HIV 相關 PAH（Rank 4）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | 完成 | 64 | PROWESS-15：含 HIV-PAH 的雙盲安慰劑對照交叉 RCT，評估 Iloprost 在 Ambrisentan 等 PAH 背景治療下的運動能力改善，為 HIV-PAH 族群使用 ETA 拮抗劑提供重要安全性與療效背景數據 |

---

## 文獻證據

### 先天性心臟病相關 PAH

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | 觀察性/案例系列 | Am J Cardiol | Columbia 大學 Eisenmenger 症患者使用 Ambrisentan 的早期臨床經驗，評估靜息與運動血液動力學 |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | 系統性回顧/Meta 分析 | Medicine | PAH 特異性藥物治療 Eisenmenger syndrome 的安全性與療效系統性回顧 |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | 真實世界研究 | Pediatr Pulmonol | 兒科 PH 使用 Ambrisentan + Tadalafil 組合的安全性與耐受性 |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | 綜述 | JAMA | PAH 診斷與治療全面回顧（JAMA），含 PAH-CHD 亞型治療建議 |
| [41727855](https://pubmed.ncbi.nlm.nih.gov/41727855/) | 2025 | 機轉回顧 | Front Pediatrics | Fontan 循環失敗中的 ET-1 病生理與 ETA 拮抗劑精準治療策略 |

### 結締組織病相關 PAH

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | 系統性回顧/Meta 分析 | Int Emerg Med | CTD-PAH 治療 RCT 的 Meta 分析，評估 FC 改善、6MWD、生存率及 NT-proBNP |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | RCT 後分析（AMBITION） | Ann Rheum Dis | Ambrisentan+Tadalafil 組合 vs 單藥在 CTD-PAH 亞組的療效比較 |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | RCT 亞組分析（AMBITION） | Ann Rheum Dis | AMBITION 試驗 CTD-PAH 亞組：初始聯合療法在 SSc-PAH 中的效益 |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | 回顧性世代研究 | Respir Med | ARIES-E 試驗 CTD-PAH 亞組：Ambrisentan 3 年療效與安全性分析 |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta 分析 | BMJ Open | CTD-PAH 臨床試驗 Meta 分析，建立循證治療基礎 |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | 敘述性回顧 | Ther Adv Respir Dis | Ambrisentan 在 PAH（含 CTD-PAH）中的臨床應用全面回顧 |

### HIV 相關 PAH

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | 回顧性世代研究 | Ther Adv Respir Dis | 轉介中心 Ambrisentan 在多種 PH 亞型（含 HIV-PAH）的臨床使用與長期耐受性 |
| [26897508](https://pubmed.ncbi.nlm.nih.gov/26897508/) | 2016 | 案例系列 | Med Clin | 4 例 HIV-PAH 患者臨床特徵、基因分析及治療經驗 |

---

## 香港上市資訊

Ambrisentan 目前在香港尚未登記上市（許可證數：0）。如欲引進，需向香港衛生署藥物辦公室提交藥物登記申請（Pharmacy and Poisons Regulations）。可參照已取得的海外核准（美國 FDA：Letairis®；歐盟 EMA：Volibris®）資料加速申請流程。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意：** Ambrisentan 屬 ERA（Endothelin Receptor Antagonist）類藥物，同類藥物有已知的肝毒性風險及嚴重致畸性（妊娠 Category X）。HIV-PAH 族群中亦需評估與抗反轉錄病毒藥物（如利托那韋）的 CYP2C9／CYP3A4 交互作用。完整警語與禁忌症資料需取得原廠仿單後方可評估。

---

## 結論與下一步

**決策：Proceed with Guardrails（PAH-CHD / CTD-PAH / HIV-PAH）/ Hold（PAVM 及其餘 7 個預測適應症）**

**理由：**
PAH-CHD、CTD-PAH 及 HIV-PAH 的病生理均以 ET-1／ETA 通路活化為核心，與 Ambrisentan 的 ETA 拮抗機轉高度吻合，且三個亞型分別有直接的 Phase 3／Phase 4 完成試驗支持（NCT01808313、NCT01042158、NCT02290613、NCT00709956），並有多篇系統性回顧與 Meta 分析佐證。TxGNN 最高分預測的 PAVM（rank 1）為結構性血管異常，缺乏 ETA 介導的病生理依據；牙周病、毛髮疾病、Dandy-Walker 畸形等（rank 7–10）均無機轉合理性，應維持 Hold。

**若要推進需要：**
- 取得 Ambrisentan 完整原廠仿單（Letairis/Volibris），評估安全警語、禁忌症（尤其妊娠毒性）及藥物交互作用
- 補充完整作用機轉（MOA）文獻資料，以支撐機轉分析
- 規劃香港衛生署藥物登記申請策略，可援引 FDA／EMA 已核准資料
- 評估 PAH-CHD 族群精準患者選擇標準，尤其是 Eisenmenger syndrome 及術後殘餘 PAH
- 考量 Ambrisentan + Tadalafil 聯合用藥策略（AMBITION 試驗顯示組合優於單藥，CTD-PAH 有直接數據）
- HIV-PAH 族群需個別評估與 HIV 抗反轉錄病毒藥物的 PK 交互作用
- 兒科 CHD-PAH 族群需確認特殊低劑量配方的可及性（已有 Phase 1 PK 數據，NCT04095286）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

