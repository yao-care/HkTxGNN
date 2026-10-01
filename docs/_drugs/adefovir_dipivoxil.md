---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil：從慢性 B 型肝炎到慢性 C 型肝炎

## 一句話總結

Adefovir Dipivoxil 是口服核苷酸類似物，原本用於慢性 B 型肝炎。TxGNN 預測它可能對**慢性 C 型肝炎 (Chronic Hepatitis C Virus Infection)** 有效，但檢索到的 10 個臨床試驗和 15 篇文獻都是 B 型肝炎研究，或 B、C 型肝炎合併討論的綜述，**沒有任何一筆直接顯示對 C 型肝炎有效**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎（許可證未載明適應症，此為依 Evidence Pack 說明的推定） |
| 預測新適應症 | 慢性 C 型肝炎 (Chronic Hepatitis C Virus Infection) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5（僅有模型預測；Evidence Pack 標示為 L4，但檢索到的證據皆非針對 HCV） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。依已知藥理，Adefovir Dipivoxil 是無環核苷酸類似物的前驅藥，其活性代謝物（二磷酸型）抑制 DNA 聚合酶與反轉錄酶，因此對 B 型肝炎病毒 (HBV) 有效。

C 型肝炎病毒 (HCV) 是 RNA 病毒，複製依賴 NS5B RNA 依賴性 RNA 聚合酶，沒有 Adefovir 會作用的 DNA 聚合酶或反轉錄步驟。**機轉上找不到直接關聯。**

分數偏高很可能只反映知識圖譜中「病毒性肝炎」節點彼此相近，不代表藥理上的實際療效。

**需要說明兩點：**
- 慢性 B 型肝炎（排名第 6）是 Adefovir 的既有適應症，只因來源資料的原適應症欄位為空才出現在預測清單中，不是真正的老藥新用發現。
- 在所有預測中，證據最完整的是 **HIV 感染**（排名第 2）：有 1 個已完成的 Phase 3 隨機雙盲試驗（NCT00001082，505 人）和多個 Phase 2 試驗，也有 RCT 文獻（JAMA 1999、AIDS 2001）。但 HIV 適應症的腎毒性風險較高，且已有更好的替代藥（如 Tenofovir）。

## 臨床試驗證據

以下是檢索到的相關試驗，相關性評估均為 C 級（非 HCV 證據）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00371761](https://clinicaltrials.gov/study/NCT00371761) | Phase 3 | 完成 | 25 | PegIntron 對比 Adefovir，用於 HBeAg 陽性慢性 B 型肝炎（台灣），Adefovir 為 HBV 對照組 |
| [NCT00013702](https://clinicaltrials.gov/study/NCT00013702) | Phase 2 | 完成 | 30 | Adefovir 加 Lamivudine，用於 HIV 合併失代償 B 型肝炎 |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 完成 | 120 | 干擾素 alpha-2b 加 Ribavirin，用於慢性 B 型肝炎，未見 Adefovir |
| [NCT00051077](https://clinicaltrials.gov/study/NCT00051077) | Phase 2 | 撤回 | 0 | Adefovir、PEG-干擾素與 Ribavirin，用於 HBV/HCV/HIV 三重感染；未收案，無資料 |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | 未知 | 600 | 早期與傳統抗病毒治療對慢性 HBV 長期預後的影響 |
| [NCT02560649](https://clinicaltrials.gov/study/NCT02560649) | Phase 4 | 未知 | 324 | 反應導向療法，NUC 治療後加 PEG-IFN，用於 HBeAg 陽性 B 型肝炎 |
| [NCT00973219](https://clinicaltrials.gov/study/NCT00973219) | 不適用 | 完成 | 151 | PEG-IFN 合併 Adefovir 或 Tenofovir，用於 HBeAg 陰性低病毒量 B 型肝炎 |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | 完成 | 104 | Adefovir 用於韓國慢性 B 型肝炎，主要指標為 HBV DNA 下降 |
| [NCT00645294](https://clinicaltrials.gov/study/NCT00645294) | Phase 1/2 | 完成 | 47 | Adefovir 單次給藥於 2–17 歲慢性 B 型肝炎兒童的藥動學與安全性 |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | 未知 | 540 | Pegasys 加 Entecavir，用於 HBeAg 陰性慢性 B 型肝炎 |

## 文獻證據

沒有 RCT，僅有綜述與間接資料；以下皆非 Adefovir 對 HCV 的直接證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | B、C 型肝炎抗病毒藥物及其對腎功能的影響；Adefovir 列於 B 型肝炎藥物 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | B、C 型肝炎現行治療與未來展望 |
| [11825542](https://pubmed.ncbi.nlm.nih.gov/11825542/) | 2002 | Review | Curr Gastroenterol Rep | 肝移植後 B、C 型肝炎的處置 |
| [25309089](https://pubmed.ncbi.nlm.nih.gov/25309089/) | 2014 | Review | World J Gastroenterol | 中國 B、C 型肝炎的臨床特徵與現行處置 |
| [15125867](https://pubmed.ncbi.nlm.nih.gov/15125867/) | 2004 | Review | J Clin Virol | 臨床使用的抗病毒藥物總覽 |
| [29743798](https://pubmed.ncbi.nlm.nih.gov/29743798/) | 2018 | Guideline | J Clin Exp Hepatol | 印度 INASL 的 B 型肝炎預防、診斷與處置共識聲明 |
| [16386596](https://pubmed.ncbi.nlm.nih.gov/16386596/) | 2005 | 臨床研究 | Transplant Proc | Adefovir 用於肝移植後 Lamivudine 抗藥性 HBV，非 HCV |
| [17530355](https://pubmed.ncbi.nlm.nih.gov/17530355/) | 2007 | 未分類 | J Gastroenterol | B、C 型肝炎抗病毒治療的抗藥性問題 |
| [24175223](https://pubmed.ncbi.nlm.nih.gov/24175223/) | 2012 | 未分類 | World J Virol | 抗病毒治療預防 B 或 C 型肝炎相關肝癌 |
| [23495004](https://pubmed.ncbi.nlm.nih.gov/23495004/) | 2013 | 未分類 | Med Res Rev | 抗病毒藥物開發現況（HCV 部分講的是直接作用抗病毒藥物，與 Adefovir 無關） |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63344 | HEPTOVANCE TABLET 10MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-64175 | APO-ADEFOVIR TABLETS 10MG | HIND WING CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中另有 Adefovir 相關腎毒性的報告，可作為風險提示：
- 長期使用的腎毒性統合分析（[PMID 27977591](https://pubmed.ncbi.nlm.nih.gov/27977591/)）
- Adefovir 引起 Fanconi 症候群與低磷血症性骨軟化症的個案（[PMID 32289307](https://pubmed.ncbi.nlm.nih.gov/32289307/)）

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上與 HCV 無直接關聯，所有檢索到的試驗與文獻都是 HBV 研究或 B、C 型肝炎合併綜述，沒有 Adefovir 對 HCV 有效的證據。
- 現今 HCV 已有直接作用抗病毒藥物（DAA）可治癒，Adefovir 不具備優勢，且有腎毒性風險。

**若要推進需要：**
- 補齊 DrugBank 作用機轉資料，並確認 HCV 的體外抗病毒活性有無實證。
- 取得香港衛生署的仿單，補齊警語與禁忌症；許可證上的核准適應症文字目前也是空的。
- 若要評估 Adefovir 的其他方向，建議改看 HIV 感染（排名第 2）。這是本 Evidence Pack 中證據最完整的一項，但需先權衡腎毒性與現有替代藥。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

