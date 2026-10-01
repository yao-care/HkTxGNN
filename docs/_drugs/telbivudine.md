---
layout: default
title: Telbivudine
parent: 僅模型預測 (L5)
nav_order: 838
evidence_level: L5
indication_count: 5
---

# Telbivudine
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

# Telbivudine：從慢性 B 型肝炎到慢性 C 型肝炎（預測）

## 一句話總結

Telbivudine 是核苷類似物抗病毒藥，目前在香港上市（品名 SEBIVO），證據包內的資料顯示其已知用途為 B 型肝炎。
TxGNN 模型預測它可能對**慢性 C 型肝炎 (Chronic hepatitis C virus infection)** 有效，預測分數很高，但檢索到的 **10 個臨床試驗**全部是 B 型肝炎試驗，**10 篇文獻**也只是 B/C 型肝炎的一般性綜述。目前沒有任何研究直接支持抗 HCV 的療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎（證據包的許可證適應症欄位為空白，此為依機轉說明推定） |
| 預測新適應症 | 慢性 C 型肝炎 (Chronic hepatitis C virus infection) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4（無任何直接針對 HCV 的研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空白）。已知 telbivudine 是胸腺嘧啶核苷類似物，抑制 HBV DNA 聚合酶（反轉錄酶）。

HCV 是 RNA 病毒，靠 NS5B（RNA 依賴性 RNA 聚合酶）複製，與 HBV 聚合酶是不同的標的。機轉上沒有明確的連結。

模型給出高分，較可能是因為 B 型與 C 型肝炎常在同一批文獻和試驗登記中一起出現（共現效應），而不是 telbivudine 真的有抗 HCV 活性。目前 HCV 的標準治療是直接作用抗病毒藥物 (DAA)。

## 臨床試驗證據

以下 10 個試驗全部是 B 型肝炎研究，沒有任何一個以 HCV 為終點。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00805675](https://clinicaltrials.gov/study/NCT00805675) | Phase 3 | 完成 | 83 | Telbivudine 合併或單用 tenofovir 治療 HBeAg 陽性 CHB 12 週的病毒動力學比較 |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | 未知 | 540 | Pegasys 合併 entecavir 治療 HBeAg 陰性 CHB，與 telbivudine 無直接關係 |
| [NCT00142298](https://clinicaltrials.gov/study/NCT00142298) | Phase 3 | 完成 | 1869 | 先前參與 telbivudine 試驗的 CHB 成人之開放標籤延伸研究 |
| [NCT03181607](https://clinicaltrials.gov/study/NCT03181607) | N/A | 未知 | 300 | 以 TDF 或 telbivudine 治療高病毒量孕婦，降低 B 肝母嬰傳染 |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | 完成 | 44 | Telbivudine 與 entecavir 治療 12 週的早期病毒動力學比較 |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | 未知 | 600 | 早期與傳統抗病毒治療對慢性 B 肝長期預後的影響（追蹤 10 年） |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | 完成 | 160 | RO7020531 在健康受試者與 CHB 患者的安全性與藥動學，非 telbivudine |
| [NCT02058108](https://clinicaltrials.gov/study/NCT02058108) | Phase 3 | 終止 | 53 | Telbivudine 用於 2 至 <18 歲 CHB 兒童與青少年的療效與安全性 |
| [NCT01083251](https://clinicaltrials.gov/study/NCT01083251) | N/A | 未知 | 120 | 維生素 D 輔助 Peg-IFN 或 telbivudine 單用治療慢性 B 肝 |
| [NCT05466071](https://clinicaltrials.gov/study/NCT05466071) | N/A | 未知 | 200 | Tenofovir alafenamide 預防高病毒量孕婦的 B 肝母嬰傳染 |

## 文獻證據

下列文獻多為 B/C 型肝炎的綜述或一般性資料，沒有 telbivudine 對 HCV 的原始研究。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19344237](https://pubmed.ncbi.nlm.nih.gov/19344237/) | 2009 | Review | Expert Rev Anti Infect Ther | B 型與 C 型肝炎處置的觀點綜述（無摘要） |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | B 肝以 pegylated interferon 為首選，lamivudine 可抑制 HBV DNA；兼論 C 肝治療展望 |
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | B/C 型肝炎與妊娠、母嬰傳染的回顧與照護建議 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | B/C 肝抗病毒藥物對腎功能的影響；telbivudine 列為 HBV 核苷類似物 |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | J Interferon Cytokine Res | Telbivudine 治療期間 CHB 患者血清 IL-37 濃度與 HBeAg 血清轉換 |
| [28845882](https://pubmed.ncbi.nlm.nih.gov/28845882/) | 2018 | 未分類（美國全國性世代資料） | J Viral Hepat | HCV 患者接受 DAA 治療後，HBV 再活化較常發生在治療結束後 |
| [18330099](https://pubmed.ncbi.nlm.nih.gov/18330099/) | 2007 | 未分類（指引） | Acta Gastroenterol Belg | 比利時肝臟研究學會 2007 年慢性 B 肝處置指引（無摘要） |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | 未分類（指引摘要） | Der Internist | 德國新指引：不適合干擾素時，可考慮 telbivudine 等單一療法治療 B 肝 |
| [21964179](https://pubmed.ncbi.nlm.nih.gov/21964179/) | 2011 | 未分類（綜述性） | Mayo Clin Proc | HIV 以外病毒（疱疹、肝炎、流感）的抗病毒藥物概述 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | 未分類（綜述性） | Paediatr Drugs | 兒童慢性肝病的藥物處置，聚焦可治癒或可能治癒的疾病 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-55624 | SEBIVO TAB 600MG | VIATRIS HEALTHCARE HONG KONG LIMITED |

此許可證的劑型與核准適應症欄位在資料中為空白。

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 查無藥物交互作用資料。

證據包的其他說明提到，telbivudine 與肌病變、周邊神經病變及抗藥性有關，且多數指引現已偏好 entecavir 或 tenofovir。使用前宜再確認最新的仿單內容。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有檢索到的試驗與文獻都是 B 型肝炎資料，沒有針對 HCV 的證據。
- 機轉上，telbivudine 抑制 HBV 聚合酶，與 HCV 的 NS5B 無關，高分很可能是 B/C 型肝炎共現造成的假象。
- 目前 HCV 已有 DAA 標準治療，沒有明確的臨床缺口需要此藥填補。

**補充觀察：**
- 同一藥物的第 2 名預測「B 型肝炎」是已知適應症，屬於找回原適應症，不是真正的老藥新用。
- 第 3 名預測「HIV」已有文獻（PMID 22024528）指出 telbivudine 無抗 HIV-1 活性。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症（目前是阻擋性缺口）。
- 補齊 DrugBank 的作用機轉資料。
- 若仍要探討 HCV，需先有體外抗 HCV 活性（如 replicon 試驗）的證據，再談臨床試驗。
- 確認 SEBIVO 在香港目前的實際供應與上市狀態。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

