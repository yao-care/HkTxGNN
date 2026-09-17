---
layout: default
title: Lactulose
parent: 高證據等級 (L1-L2)
nav_order: 430
evidence_level: L2
indication_count: 5
---

# Lactulose
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

# Lactulose：從肝性腦病變到阻塞性黃疸（多重候選適應症）

## 一句話總結

Lactulose 是傳統用於肝性腦病變、慢性便秘的滲透性瀉劑/腸道酸化劑（本次候選為 multi-indication 評估，涵蓋 TxGNN 預測的 5 個新適應症）。其中證據最紮實的是**阻塞性黃疸 (Obstructive Jaundice)**，有 **1 個已完成的 Phase 4 臨床試驗**與 **20 篇文獻**（含 1 篇多中心 RCT）支持；其餘 4 個預測——包括分數最高的 acute urate nephropathy——目前僅為模型純預測，無任何臨床或文獻佐證。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 查無本地許可證資料（本藥未在本地上市）；文獻脈絡顯示 lactulose 已知用於肝性腦病變（腸道去污/降氨）與慢性便秘 |
| 預測新適應症 | 阻塞性黃疸 (Obstructive Jaundice)（本次 5 個候選中證據最強者，非 TxGNN 原始分數第一名） |
| TxGNN 預測分數 | 99.53%（obstructive jaundice，全域排名 8522） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold（Research Question 階段，尚未達 Proceed 門檻） |

## 其他預測適應症一覽

Evidence Pack 屬 multi-indication 候選（candidate_id: TW-DB00581-multi），完整列出 5 個 TxGNN 預測供比較：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 1 | Acute urate nephropathy | 99.89% | L5 | S0 | Hold |
| 2 | Nephrolithiasis | 99.78% | L5 | S0 | Hold |
| 3 | **Obstructive jaundice** | 99.53% | L2 | S2 | Research Question |
| 4 | Bile duct disease | 99.47% | L3 | S1 | Research Question |
| 5 | Biliary tract disease | 99.38% | L4 | S0 | Hold |

分數最高的兩個候選（acute urate nephropathy、nephrolithiasis）完全查無臨床試驗或文獻，屬純知識圖譜拓樸相似性推論，暫不具研究價值。以下章節聚焦證據最完整的**阻塞性黃疸**。

## 為什麼這個預測合理？

官方 MOA 欄位缺乏正式收錄的作用機轉描述，但根據本次證據回顧整理的機轉假說：lactulose 在腸道被菌叢發酵為酸，降低腸道 pH、抑制產氨/產內毒素菌叢，減少內毒素經腸道吸收——此機轉與其在肝性腦病變的既有適應症一致。

阻塞性黃疸病人因膽鹽未能進入腸道，腸道屏障與 Kupffer 細胞功能受損，內毒素血症被認為是術後腎功能不全（類肝腎症候群損傷）的關鍵路徑。因此 lactulose 的腸道去污（gut decontamination）作用在機轉上具合理延伸性，也解釋了為何多篇文獻聚焦於「術前給予 lactulose 預防阻塞性黃疸手術後腎功能不全」這個具體臨床情境，而非治療阻塞性黃疸本身。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01090193](https://clinicaltrials.gov/study/NCT01090193) | Phase 4 | 完成 | 20 | 觀察阻塞性黃疸病人的腎臟組織病理變化，屬病理描述性研究，未介入給予 lactulose |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | RCT（多中心） | Br J Surg | 102 名阻塞性黃疸手術病人隨機分組，術前 lactulose vs 去氧膽酸鈉 vs 對照，評估預防術後腎功能不全 |
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | 前瞻性對照研究 | Br J Surg | 24 名病人，術前口服 lactulose 顯著降低門靜脈及全身內毒素血症 |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | 動物實驗 | J Surg Res | 兔隻膽管結紮模型，lactulose 降低全身性內毒素血症 |
| [17708248](https://pubmed.ncbi.nlm.nih.gov/17708248/) | 2007 | 世代研究 | Hepatogastroenterology | 急性阻塞性黃疸死亡率/併發症預測因子，討論預防性措施 |
| [15782993](https://pubmed.ncbi.nlm.nih.gov/15782993/) | 2005 | 回顧 | Hepatogastroenterology | 阻塞性黃疸腎衰竭之預防，強調術前水分補充與 lactulose 給藥必要性 |
| [29428098](https://pubmed.ncbi.nlm.nih.gov/29428098/) | 2018 | Review | HBPD Int | 阻塞性黃疸病理生理學與圍術期處置總論 |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Review | Scand J Gastroenterol Suppl | Lactulose 於腎功能不全的角色，指出腎保護效果臨床上未獲一致證實 |
| [9174857](https://pubmed.ncbi.nlm.nih.gov/9174857/) | 1997 | Review | HPB Surgery | 阻塞性黃疸病人的免疫功能異常與相關介質 |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | 動物實驗 | Pediatr Surg Int | 大鼠模型，melatonin+lactulose 對阻塞性黃疸肝腎的保護作用 |
| [8944448](https://pubmed.ncbi.nlm.nih.gov/8944448/) | 1996 | 臨床+動物實驗 | Br J Surg | 阻塞性黃疸腸道屏障功能障礙，內在膽道引流可逆轉此現象 |

## 香港上市資訊

目前無香港上市許可證登記（`market_status`: 未上市，`total_licenses`: 0）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold（Research Question 階段）**

**理由：**
阻塞性黃疸候選有 1 個完成的臨床觀察研究及多篇支持性文獻（含 1 篇多中心 RCT），機轉與 lactulose 既有肝性腦病變適應症一脈相承，但現有 RCT 證據聚焦於「預防阻塞性黃疸手術後腎功能不全」的輔助角色，並非直接治療阻塞性黃疸本身，尚不足以支持 Proceed。其餘 4 個候選（含 TxGNN 分數最高的 acute urate nephropathy、nephrolithiasis）純屬模型預測，無機轉、臨床或文獻佐證，維持 Hold。

**若要推進需要：**
- TFDA/香港仿單警語與禁忌症資料（DG001，Blocking：目前無法進入 S1 安全性初評）
- 正式收錄的藥物作用機轉資料（DG002）
- 針對「lactulose 腸道去污對阻塞性黃疸術後腎保護效果」設計前瞻性 RCT，確認因果效益
- 釐清 acute urate nephropathy、nephrolithiasis、biliary tract disease 的機轉合理性後，再決定是否納入後續證據收集
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

